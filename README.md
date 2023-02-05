# RedisPubSubNewsSystem

A news publishing system based on the Redis pub/sub implementation.

The frontend `index.html` uses sockets library to connect with the node backend. The backend is basically the subscriber that is toggled using the frontend. Once a subscription is made, a subscription is made for that specific topic. 

The publisher is a Python script that uses our [dataset](https://www.kaggle.com/datasets/amananandrai/ag-news-classification-dataset), to publish a news article related to a specific topic. This publishing is cached using the Redis cache system and the dataset is not searched again if a news article that is requested is already present in the cache. 

The system diagram for this project is shown below.

![image](https://user-images.githubusercontent.com/39828020/216795743-311fcfc2-4e6d-4e9e-84a3-4e0639664122.png)
