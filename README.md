- this is fastapi prectice whereby we use sentiment analysis 
### DEPENDACIES:
1. we used poetry to install all our dependacies. to install poetry we use: 

pip install poetry 
2. to initialize poetry into your environment and fill in the values.

poetry init 
3. using poetry to install fastapi and all other dependacies.


poetry add fastapi uvicorn
poetry add vadersentiment
4. to use a dockerfile you first have to install docker on your system. you can install docker desktop on windows, then you create your docker image with the use of dockerfile
5. to build your docker container you use the following command


docker build -t [image_name]
6. to run your docker image you use the command below.


docker run -p [port_num_in_your_image] [image_name]
