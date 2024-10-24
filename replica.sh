#  1. create folder "Data"
#  2. create 3 sub folders within "Data" : rs1,rs2,rs3
#  3. open cmd in C:\Program Files\MongoDB\Server\4.4\bin
#  4."utube" = server name

start mongod -replSet utube -logpath F:\NGT\Replica\Data\rs1\1.log --dbpath F:\NGT\Replica\Data\rs1 --port 27018

start mongod -replSet utube -logpath F:\NGT\Replica\Data\rs2\2.log --dbpath F:\NGT\Replica\Data\rs2 --port 27019

start mongod -replSet utube -logpath F:\NGT\Replica\Data\rs3\3.log --dbpath F:\NGT\Replica\Data\rs3 --port 27020

# Primary=================================================
# 5. again open cmd in C:\Program Files\MongoDB\Server\4.4\bin
mongo --port 27018

# 6. Configure Server
config={_id:"utube",members:[{_id:0,host:"localhost:27018"},{_id:1,host:" localhost:27019"}, {_id:2 host:"localhost:27020"}]}

rs.initiate(config)

rs.status()

shift to primary ( 27018 )

# create database and collection and insert docs
use test123
db.createCollection("cust")
db.cust.insert({"name":"hardik"})