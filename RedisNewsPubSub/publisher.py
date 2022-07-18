


#import necessary modules
import csv
import redis

className = -1
article = []
message = ""

redisClient = redis.StrictRedis(host='localhost',  port=6379,db=0)

while True:
    className = -1
    topic = input("Enter Topic Name: ")
    message = " " #reset message value
    article = [] #reset article value
    if(redisClient.hget("CacheTopics", topic)):
        print("Cache Hit")
        print("Topic: ",topic)
        value = redisClient.hget("CacheTopics", topic).decode('UTF-8')  #convert bytes to string
        
        desc = value.split(",") #split the string using , 
        message = topic + "," + desc[1]  
        print("Class: ",desc[0]) 
        print("Description: ",desc[1]) 
        bmessage = bytes(message, 'utf-8') #converting string to bytesstring  
        redisClient.publish(desc[0],bmessage)
    else:
        #code to run if cache miss

        
        print("Cache miss")

        with open('test.csv','rt')as f: #search the topic in file
        # with open('testSmall.csv','rt')as f: #search the topic in file
            data = csv.reader(f)
            for row in data:
                    if(topic == (row[1])):
                        article = row
                        print("Topic: ",article[1]) #topic
                        print("Desc: ",article[2]) #description
                        className = article[0]
                        message = topic + "," + article[2]
                        bmessage = bytes(message, 'utf-8') #converting string to bytesstring                        
                        redisClient.publish(article[0],bmessage)

        if(className != -1):
            print("class of the article: ",className)

            with open('test.csv','rt')as g:       #cache all topics of that class
            # with open('testSmall.csv','rt')as g:       #cache all topics of that class
                data = csv.reader(g)  
                for row in data:
                    if(row[0] == className):
                        redisClient.hset("CacheTopics", row[1],row[0]+","+row[2])
        else:
            print("Topic not found")


    
    