# Agree2Disagree

### About Us
- We are a dedicated group of innovators on a mission to provide you the user the power to fight for your privacy laws and data by giving you th eability to summarize and provide insights about user agreements 

### Mission 
- In a world where big tech and many other companies misuse user data without them even knowing, we plan to use this platform to inform and educate users what they are signing up for when agreeing to user agreements 

### Vision 
- Our vision is that this platform we develop will allow users to get educated and be more cautious when agreeing to terms and services and become more concious about how vauable their user data is and encouurage them to take control of it. 
- Eventually we envision a world where people will be able to agree and disagree to specific things in user agreements instead of agreeing to all of the terms on the agreements.

- showcases the flow of our LLM application

Right now it is shows the general flow of the app
will be eventually add prompts and make this more precise to form a fully functional prompt eng flow chart

<img width="1172" height="964" alt="image" src="https://github.com/user-attachments/assets/fea14ffc-3d1a-4d89-b991-02b54fe48ad0" />

Plan for Generating Risk assessment score

Once Summary is generated and validation check is passed
we will make LLLM generate the risk scores for the categories of Data collection, Data sharing and Security practices
we generate the scores above for at least 50 user agreements and set up our data and normalize it
after normalizing the data we run it through HDBSCAN clustering algorithm to cluster low, moderate and high risk user agreements into their respective clusters
we will run the HDBSCAN clustering algorithm every time a new user agreement is fed into the model, hence making our clustering algorithm better every time a new user agreement is passed in
