# Challenge 2
## Problem statement


We need to write code that will query the meta data of an instance within AWS and provide a json formatted output.



## Language 

  
I will be using Python to showcase my proficiency in language . I will be using the rest api of AWS to get the metadata



## Approach

 


  The AWS have an API which when run within EC2 (AWS instance) returns metadata
  
>http://169.254.169.254/latest/meta-data/



This Api will return all the top level key and we will iterate the list of keys with same API with key added at end. Some keys may return array of keys.


>http://169.254.169.254/latest/meta-data/{key}



Then we build json object to keep track of all key and values. This will help to return value for individual key. We can even transverse the JSON tree to find the valuefor the given key.
 For further info refer to [AWS docs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html)








## Bonus Points

  


The code allows for a particular data key to be retrieved individually

  

  
