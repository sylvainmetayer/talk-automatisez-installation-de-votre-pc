#!/usr/bin/env python3

from diagrams import Cluster, Diagram
from diagrams.aws.analytics import ElasticsearchService
from diagrams.aws.compute import (ApplicationAutoScaling, EC2AutoScaling,
                                  EC2ContainerRegistry,
                                  ElasticKubernetesService)
from diagrams.aws.database import Elasticache, RDSMysqlInstance
from diagrams.aws.management import Cloudwatch, SystemsManager
from diagrams.aws.network import (ALB, NLB, CloudFront, InternetGateway,
                                  NATGateway, Route53)
from diagrams.aws.security import ACM, KMS, WAF, SecretsManager
from diagrams.aws.storage import Backup
from diagrams.onprem.client import Client, Users
from diagrams.onprem.network import Internet


def public_subnet_links(alb, igw):
    igw >> alb
    nat >> igw >> internet


with Diagram("Infrastructure", show=False, direction="BT"):
    internet = Internet("External registrar")
    users = Client("Users")
    admins = Users('Admins')
    users >> internet
    with Cluster('AWS Cloud'):
        with Cluster('Region eu-west-1'):
            cloudwatch = Cloudwatch('Cloudwatch')
            igw = InternetGateway('IG')
            dns = Route53("dns")
            cloudfront = CloudFront('Distribution')
            waf = WAF('WAF')
            ssm = SystemsManager('Session manager')
            secret_manager = SecretsManager('SecretManager')
            kms = KMS('KMS')
            aws_backup = Backup('AWS Backup')

            ecr = EC2ContainerRegistry('ECR')
            admins >> ssm

            internet >> dns
            dns >> cloudfront
            cloudfront >> ACM('TLS Certificate')
            cloudfront >> waf
            waf >> igw
            with Cluster('VPC'):
                with Cluster('AZ 1'):
                    with Cluster('Public subnet eu-west-1a'):
                        alb = ALB('ALB')
                        nat = NATGateway('NAT')
                        public_subnet_links(alb, igw)
                    with Cluster('Private subnet eu-west-1a'):
                        tools_server_az1 = EC2AutoScaling('Tools server')
                        ssm >> tools_server_az1
                        eks_az1 = ElasticKubernetesService('Cluster')
                        alb >> eks_az1
                        with Cluster('Node group'):
                            asg_cms = ApplicationAutoScaling('CMS')
                            asg_front = ApplicationAutoScaling('FRONT')
                            node_group_az1 = [
                                asg_cms, asg_front
                            ]
                            eks_az1 >> node_group_az1
                            node_group_az1 >> nat
                        with Cluster('NoSQL database layer'):
                            redis_primary_az1 = Elasticache('ElastiCache')
                            node_group_az1 >> redis_primary_az1
                        with Cluster('RDS MySQL Cluster - CMS'):
                            mysql_primary_az1 = RDSMysqlInstance('Primary')
                            node_group_az1 >> mysql_primary_az1
                        with Cluster('ElasticSearch Domain'):
                            elastic_search_az1 = ElasticsearchService()
                            node_group_az1 >> elastic_search_az1
