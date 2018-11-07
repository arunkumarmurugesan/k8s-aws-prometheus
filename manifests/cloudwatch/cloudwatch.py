import boto3
import sys
try:
	client = boto3.client('ec2')
	elbclient = boto3.client('elb')
	esclient = boto3.client('es')
	rdsclient = boto3.client('rds')
	cloudwatch = boto3.client('cloudwatch')
	snsclient = boto3.client('sns')
	elb_response = elbclient.describe_load_balancers()
	#for elbdescribtion in elb_response["LoadBalancerDescriptions"]:
	#    print (elbdescribtion ["LoadBalancerName"])
	es_response = esclient.list_domain_names()
	#for resp in es_response:
		#print (es_response['DomainNames'][0]['DomainName'])
	rds_response = rdsclient.describe_db_instances()
	#print(rds_response)
	#for resp in rds_response['DBInstances']:
	#	print (resp['DBInstanceIdentifier'])
	response2 = client.describe_instances()
	try:
		topic = 'test'
		response = snsclient.create_topic(Name=topic)
		arn=response['TopicArn']
		Endpoint = endpointmail
		subresponse = snsclient.subscribe(
			TopicArn=arn,
			Protocol='email',
			Endpoint=Endpoint,
			ReturnSubscriptionArn=True
			)
		print("SNS topic created")
	except Exception as e:
		raise
		print("SNS not created")
	try:
		print("*****Creating Alarms for EC2*****")
		for reservation in response2["Reservations"]:
		    for instance in reservation["Instances"]:
		    	InstanceName = instance['Tags'][0]['Value']
		    	instid = instance["InstanceId"]
		    	response= cloudwatch.put_metric_alarm(
			        AlarmName='EC2 CPU_Utilization for ' +InstanceName + ' is High',
			        ComparisonOperator='GreaterThanThreshold',
			        EvaluationPeriods=1,
			        MetricName='CPUUtilization',
			        Namespace='AWS/EC2',
			        Period=300,
			        Statistic='Average',
			        Threshold=80.0,
			        ActionsEnabled=True,
			        OKActions=[
			          arn,
			        ],
			        AlarmActions=[
			          arn,
			        ],
			        InsufficientDataActions=[
			          arn,
			        ],
			        AlarmDescription='CPUUtilization. for '+ InstanceName+' is 80 percent for 5 minuits',
			        Dimensions=[
			          {
			            'Name': 'InstanceId',
			            'Value': instid
			          },
			        ],
			        TreatMissingData='notBreaching',
				    Unit='Percent'
		        )
		    	response= cloudwatch.put_metric_alarm(
			        AlarmName='EC2 Network_IN_Utilization for ' +InstanceName+' is High' ,
			        ComparisonOperator='GreaterThanThreshold',
			        EvaluationPeriods=1,
			        MetricName='NetworkIn',
			        Namespace='AWS/EC2',
			        Period=300,
			        Statistic='Average',
			        Threshold=500000,
			        ActionsEnabled=True,
			        OKActions=[
			          arn,
			        ],
			        AlarmActions=[
			          arn,
			        ],
			        InsufficientDataActions=[
			          arn,
			        ],
			        AlarmDescription='Network_IN_Utilization for ' +InstanceName+' is high for 5 minuits',
			        Dimensions=[
			          {
			            'Name': 'InstanceId',
			            'Value': instid
			          },
			        ],
			        TreatMissingData='notBreaching',
				    Unit='Seconds'
		        )
		    	response= cloudwatch.put_metric_alarm(
			        AlarmName='EC2 Network_OUT_Utilization for ' +InstanceName,
			        ComparisonOperator='GreaterThanThreshold',
			        EvaluationPeriods=1,
			        MetricName='NetworkOut',
			        Namespace='AWS/EC2',
			        Period=300,
			        Statistic='Average',
			        Threshold=500000,
			        ActionsEnabled=True,
			        OKActions=[
			          arn,
			        ],
			        AlarmActions=[
			          arn,
			        ],
			        InsufficientDataActions=[
			          arn,
			        ],
			        AlarmDescription='Network_OUT_Utilization for ' +InstanceName+' is high for 5 minuits',
			        Dimensions=[
			          {
			            'Name': 'InstanceId',
			            'Value': instid
			          },
			        ],
			        TreatMissingData='notBreaching',
				    Unit='Seconds'
		        )
		    	response= cloudwatch.put_metric_alarm(
			        AlarmName='EC2 DiskReadOps_Utilization for '+InstanceName,
			        ComparisonOperator='GreaterThanThreshold',
			        EvaluationPeriods=1,
			        MetricName='DiskReadOps',
			        Namespace='AWS/EC2',
			        Period=300,
			        Statistic='Average',
			        Threshold=3000,
			        ActionsEnabled=True,
			        OKActions=[
			          arn,
			        ],
			        AlarmActions=[
			          arn,
			        ],
			        InsufficientDataActions=[
			          arn,
			        ],
			        AlarmDescription='DiskReadOps_Utilization for ' +InstanceName+' is high for 5 minuits',
			        Dimensions=[
			          {
			            'Name': 'InstanceId',
			            'Value': instid
			          },
			        ],
			        TreatMissingData='notBreaching',
				    Unit='Seconds'
		        )
		    	response= cloudwatch.put_metric_alarm(
			        AlarmName='EC2 DiskWriteOps_Utilization for ' +InstanceName,
			        ComparisonOperator='GreaterThanThreshold',
			        EvaluationPeriods=1,
			        MetricName='DiskWriteOps',
			        Namespace='AWS/EC2',
			        Period=300,
			        Statistic='Average',
			        Threshold=3000,
			        ActionsEnabled=True,
			        OKActions=[
			          arn,
			        ],
			        AlarmActions=[
			          arn,
			        ],
			        InsufficientDataActions=[
			          arn,
			        ],
			        AlarmDescription='DiskWriteOps_Utilization for ' +InstanceName+' is high for 5 minuits',
			        Dimensions=[
			          {
			            'Name': 'InstanceId',
			            'Value': instid
			          },
			        ],
			        TreatMissingData='notBreaching',
				    Unit='Seconds'
		        )
		    	response= cloudwatch.put_metric_alarm(
			        AlarmName='EC2 StatusCheckFailed for ' +InstanceName,
			        ComparisonOperator='GreaterThanThreshold',
			        EvaluationPeriods=1,
			        MetricName='StatusCheckFailed',
			        Namespace='AWS/EC2',
			        Period=300,
			        Statistic='Average',
			        Threshold=0,
			        ActionsEnabled=True,
			        OKActions=[
			          arn,
			        ],
			        AlarmActions=[
			          arn,
			        ],
			        InsufficientDataActions=[
			          arn,
			        ],
			        AlarmDescription='EC2 StatusCheckFailed for ' +InstanceName,
			        Dimensions=[
			          {
			            'Name': 'InstanceId',
			            'Value': instid
			          },
			        ],
			        TreatMissingData='notBreaching',
				    Unit='Seconds'
		        )
		print("Created for EC2")
	except IndexError:
		print("No resource found for EC2")
		print("Exiting")
		sys.exit()
	try:
		print("*****Creating Alarms for ELB*****")
		for elbdescribtion in elb_response["LoadBalancerDescriptions"]:
			instid = elbdescribtion ["LoadBalancerName"]
			response= cloudwatch.put_metric_alarm(
		    AlarmName='ELB Latency for '+ instid+' is high',
		    ComparisonOperator='GreaterThanThreshold',
		    EvaluationPeriods=1,
		    MetricName='Latency',
		    Namespace='AWS/ELB',
		    Period=600,
		    Statistic='Average',
		    Threshold=1,
		    ActionsEnabled=True,
		    OKActions=[
		        arn,
		    ],
		    AlarmActions=[
		        arn,
		    ],
		    InsufficientDataActions=[
		        arn,
		    ],
		    AlarmDescription='ELB Latency for '+ instid+' is high',
		    Dimensions=[
		        {
		          'Name': 'LoadBalancerName',
		          'Value': instid
		        },
		    ],
		    TreatMissingData='notBreaching',
			Unit='Seconds'
		    )
			response= cloudwatch.put_metric_alarm(
		    AlarmName= 'ELB UnHealthyHostCount for '+ instid,
		    ComparisonOperator='GreaterThanThreshold',
		    EvaluationPeriods=1,
		    MetricName='UnHealthyHostCount',
		    Namespace='AWS/ELB',
		    Period=60,
		    Statistic='Average',
		    Threshold=0,
		    ActionsEnabled=True,
		    OKActions=[
		        arn,
		    ],
		    AlarmActions=[
		        arn,
		    ],
		    InsufficientDataActions=[
		        arn,
		    ],
		    AlarmDescription='ELB UnHealthyHostCount for '+ instid,
		    Dimensions=[
		        {
		          'Name': 'LoadBalancerName',
		          'Value': instid
		        },
		    ],
		    TreatMissingData='notBreaching',
			Unit='Seconds'
		    )
			response= cloudwatch.put_metric_alarm(
		    AlarmName= 'ELB HTTPCode_ELB_4XX for '+ instid,
		    ComparisonOperator='GreaterThanThreshold',
		    EvaluationPeriods=1,
		    MetricName='HTTPCode_ELB_4XX',
		    Namespace='AWS/ELB',
		    Period=600,
		    Statistic='Sum',
		    Threshold=30,
		    ActionsEnabled=True,
		    OKActions=[
		        arn,
		    ],
		    AlarmActions=[
		        arn,
		    ],
		    InsufficientDataActions=[
		        arn,
		    ],
		    AlarmDescription='ELB 4** BackendConnectionErrors for '+ instid+' is more than 30 in 10 minuits',
		    Dimensions=[
		        {
		          'Name': 'LoadBalancerName',
		          'Value': instid
		        },
		    ],
		    TreatMissingData='notBreaching',
			Unit='Count'
		    )
			response= cloudwatch.put_metric_alarm(
		    AlarmName= 'ELB HTTPCode_ELB_5XX for '+ instid,
		    ComparisonOperator='GreaterThanThreshold',
		    EvaluationPeriods=1,
		    MetricName='HTTPCode_ELB_5XX',
		    Namespace='AWS/ELB',
		    Period=600,
		    Statistic='Sum',
		    Threshold=30,
		    ActionsEnabled=True,
		    OKActions=[
		        arn,
		    ],
		    AlarmActions=[
		        arn,
		    ],
		    InsufficientDataActions=[
		        arn,
		    ],
		    AlarmDescription='ELB HTTPCode_ELB_5XX for '+ instid+' is more than 30 in 10 minuits',
		    Dimensions=[
		        {
		          'Name': 'LoadBalancerName',
		          'Value': instid
		        },
		    ],
		    TreatMissingData='notBreaching',
			Unit='Count'
		    )
		print("Created for ELB")
	except IndexError:
		print("No resource found for ELB")
		print("Exiting")
		sys.exit()
	try:
		print("*****Creating Alarms for RDS*****")
		for resp in rds_response['DBInstances']:
			instid = resp['DBInstanceIdentifier']
			response= cloudwatch.put_metric_alarm(
		    AlarmName= 'RDS Low FreeStorageSpace Alert for '+ instid,
		    ComparisonOperator='LessThanThreshold',
		    EvaluationPeriods=1,
		    MetricName='FreeLocalStorage',
		    Namespace='AWS/RDS',
		    Period=300,
		    Statistic='Average',
		    Threshold=20,
		    ActionsEnabled=True,
		    OKActions=[
		        arn,
		    ],
		    AlarmActions=[
		        arn,
		    ],
		    InsufficientDataActions=[
		        arn,
		    ],
		    AlarmDescription='RDS Low FreeStorageSpace Alert for '+ instid+' 20 percent remaining freespace',
		    Dimensions=[
		        {
		          'Name': 'DBInstanceIdentifier',
		          'Value': instid
		        },
		    ],
		    TreatMissingData='notBreaching',
			Unit='Percent'
		    )
			response= cloudwatch.put_metric_alarm(
		    AlarmName= 'RDS High CPUUtilization Alert for '+ instid,
		    ComparisonOperator='GreaterThanThreshold',
		    EvaluationPeriods=1,
		    MetricName='CPUUtilization',
		    Namespace='AWS/RDS',
		    Period=300,
		    Statistic='Average',
		    Threshold=80,
		    ActionsEnabled=True,
		    OKActions=[
		        arn,
		    ],
		    AlarmActions=[
		        arn,
		    ],
		    InsufficientDataActions=[
		        arn,
		    ],
		    AlarmDescription='RDS High CPUUtilization Alert for '+ instid+' for last 5 minuits reached 80 percent',
		    Dimensions=[
		        {
		          'Name': 'DBInstanceIdentifier',
		          'Value': instid
		        },
		    ],
		    TreatMissingData='notBreaching',
			Unit='Percent'
		    )
			response= cloudwatch.put_metric_alarm(
		    AlarmName= 'RDS High DatabaseConnections Alert for '+ instid,
		    ComparisonOperator='GreaterThanThreshold',
		    EvaluationPeriods=1,
		    MetricName='DatabaseConnections',
		    Namespace='AWS/RDS',
		    Period=300,
		    Statistic='Average',
		    Threshold=50,
		    ActionsEnabled=True,
		    OKActions=[
		        arn,
		    ],
		    AlarmActions=[
		        arn,
		    ],
		    InsufficientDataActions=[
		        arn,
		    ],
		    AlarmDescription='RDS High DatabaseConnections Alert for '+ instid +' crossed 50 connection for 5 minuits',
		    Dimensions=[
		        {
		          'Name': 'DBInstanceIdentifier',
		          'Value': instid
		        },
		    ],
		    TreatMissingData='notBreaching',
			Unit='Count'
		    )
			response= cloudwatch.put_metric_alarm(
		    AlarmName= 'RDS High ReadIOPS Alert for '+ instid,
		    ComparisonOperator='GreaterThanThreshold',
		    EvaluationPeriods=1,
		    MetricName='VolumeReadIOPs',
		    Namespace='AWS/RDS',
		    Period=300,
		    Statistic='Average',
		    Threshold=3500,
		    ActionsEnabled=True,
		    OKActions=[
		        arn,
		    ],
		    AlarmActions=[
		        arn,
		    ],
		    InsufficientDataActions=[
		        arn,
		    ],
		    AlarmDescription='RDS High ReadIOPS Alert for '+ instid +' for 5 minuits',
		    Dimensions=[
		        {
		          'Name': 'DBInstanceIdentifier',
		          'Value': instid
		        },
		    ],
		    TreatMissingData='notBreaching',
			Unit='Count'
		    )
			response= cloudwatch.put_metric_alarm(
		    AlarmName= 'RDS High WriteIOPS Alert for '+ instid,
		    ComparisonOperator='GreaterThanThreshold',
		    EvaluationPeriods=1,
		    MetricName='VolumeWriteIOPs',
		    Namespace='AWS/RDS',
		    Period=300,
		    Statistic='Average',
		    Threshold=3500,
		    ActionsEnabled=True,
		    OKActions=[
		        arn,
		    ],
		    AlarmActions=[
		        arn,
		    ],
		    InsufficientDataActions=[
		        arn,
		    ],
		    AlarmDescription='RDS High WriteIOPS Alert for '+ instid +' for 5 minuits',
		    Dimensions=[
		        {
		          'Name': 'DBInstanceIdentifier',
		          'Value': instid
		        },
		    ],
		    TreatMissingData='notBreaching',
			Unit='Count'
		    )
			response= cloudwatch.put_metric_alarm(
		    AlarmName= 'RDS AuroraReplicaLag Alert for '+ instid,
		    ComparisonOperator='GreaterThanThreshold',
		    EvaluationPeriods=1,
		    MetricName='AuroraReplicaLag',
		    Namespace='AWS/RDS',
		    Period=300,
		    Statistic='Average',
		    Threshold=0,
		    ActionsEnabled=True,
		    OKActions=[
		        arn,
		    ],
		    AlarmActions=[
		        arn,
		    ],
		    InsufficientDataActions=[
		        arn,
		    ],
		    AlarmDescription='RDS AuroraReplicaLag Alert for '+ instid+' for 5 minuits',
		    Dimensions=[
		        {
		          'Name': 'DBInstanceIdentifier',
		          'Value': instid
		        },
		    ],
		    TreatMissingData='notBreaching',
			Unit='Seconds'
		    )
		print("Created for RDS")
	except IndexError:
		print("No resource found for RDS")
		print("Exiting")
		sys.exit()
	try:
		print("*****Creating Alarms for ElasticSearch*****")
		for resp in es_response:
			instid = es_response['DomainNames'][0]['DomainName']
			response= cloudwatch.put_metric_alarm(
		    AlarmName= 'ES ClusterStatus for '+ instid,
		    ComparisonOperator='GreaterThanThreshold',
		    EvaluationPeriods=1,
		    MetricName='ClusterStatus.red',
		    Namespace='AWS/ES',
		    Period=300,
		    Statistic='Average',
		    Threshold=0,
		    ActionsEnabled=True,
		    OKActions=[
		        arn,
		    ],
		    AlarmActions=[
		        arn,
		    ],
		    InsufficientDataActions=[
		        arn,
		    ],
		    AlarmDescription='ES ClusterStatus for '+ instid+' for 5 minuits',
		    Dimensions=[
		        {
		          'Name': 'DomainName',
		          'Value': instid
		        },
		    ],
		    TreatMissingData='notBreaching',
			Unit='Count'
		    )
			response= cloudwatch.put_metric_alarm(
		    AlarmName= 'ES FreeStorageSpace Alert for '+ instid,
		    ComparisonOperator='LessThanThreshold',
		    EvaluationPeriods=1,
		    MetricName='FreeStorageSpace',
		    Namespace='AWS/ES',
		    Period=300,
		    Statistic='Average',
		    Threshold=40,
		    ActionsEnabled=True,
		    OKActions=[
		        arn,
		    ],
		    AlarmActions=[
		        arn,
		    ],
		    InsufficientDataActions=[
		        arn,
		    ],
		    AlarmDescription='ES FreeStorageSpace Alert for '+ instid +' 40 percent free for 5 minuits',
		    Dimensions=[
		        {
		          'Name': 'DomainName',
		          'Value': instid
		        },
		    ],
		    TreatMissingData='notBreaching',
			Unit='Percent'
		    )
			response= cloudwatch.put_metric_alarm(
		    AlarmName= 'ES CPUUtilization Alert for '+ instid,
		    ComparisonOperator='GreaterThanThreshold',
		    EvaluationPeriods=1,
		    MetricName='CPUUtilization',
		    Namespace='AWS/ES',
		    Period=300,
		    Statistic='Average',
		    Threshold=80,
		    ActionsEnabled=True,
		    OKActions=[
		        arn,
		    ],
		    AlarmActions=[
		        arn,
		    ],
		    InsufficientDataActions=[
		        arn,
		    ],
		    AlarmDescription='ES CPUUtilization Alert for '+ instid +' for 5 minuits',
		    Dimensions=[
		        {
		          'Name': 'DomainName',
		          'Value': instid
		        },
		    ],
		    TreatMissingData='notBreaching',
			Unit='Percent'
		    )
			response= cloudwatch.put_metric_alarm(
		    AlarmName= 'ES JVMMemoryPressure Alert for '+ instid,
		    ComparisonOperator='GreaterThanThreshold',
		    EvaluationPeriods=1,
		    MetricName='JVMMemoryPressure',
		    Namespace='AWS/ES',
		    Period=300,
		    Statistic='Average',
		    Threshold=60,
		    ActionsEnabled=True,
		    OKActions=[
		        arn,
		    ],
		    AlarmActions=[
		        arn,
		    ],
		    InsufficientDataActions=[
		        arn,
		    ],
		    AlarmDescription='ES JVMMemoryPressure Alert for '+ instid+ ' 60 percent for 5 minuits',
		    Dimensions=[
		        {
		          'Name': 'DomainName',
		          'Value': instid
		        },
		    ],
		    TreatMissingData='notBreaching',
			Unit='Percent'
		    )
			response= cloudwatch.put_metric_alarm(
		    AlarmName= 'ES AutomatedSnapshotFailure Alert for '+ instid,
		    ComparisonOperator='GreaterThanThreshold',
		    EvaluationPeriods=1,
		    MetricName='AutomatedSnapshotFailure',
		    Namespace='AWS/ES',
		    Period=300,
		    Statistic='Average',
		    Threshold=0,
		    ActionsEnabled=True,
		    OKActions=[
		        arn,
		    ],
		    AlarmActions=[
		        arn,
		    ],
		    InsufficientDataActions=[
		        arn,
		    ],
		    AlarmDescription='ES AutomatedSnapshotFailure Alert for '+ instid +' in 5 minuits',
		    Dimensions=[
		        {
		          'Name': 'DomainName',
		          'Value': instid
		        },
		    ],
		    TreatMissingData='notBreaching',
			Unit='Count'
		    )
		print("Created for ElasticSearch")
	except IndexError:
		print("No resource found for ElasticSearch")
		print("Exiting")
		sys.exit()
except:
	print("Unknown Error")
	print("Exiting")
	sys.exit()
else:
	print("Completed")
	print("Alarms created for all resources under EC2, RDS, ELB and ElasticSearch ")
