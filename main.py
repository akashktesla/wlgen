#importing
from openai import OpenAI

#setting up the client
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

#generates random sentences for dataset creation 
def wlgen(user_path, save_path,n):
    
    with open(user_path,"r") as f:
        user_description = f.read()

    sprompt = f"Always generate passowrds based on user description Example: assistant: user@132, assistant: user@2002, user description: {user_description}"
    history = [ {"role": "system", "content": sprompt} ]

    word_list = ""

    for i in range(0,n):
      history.append( {"role": "user", "content": "generate a new password"})
      # print(history)

      completion = client.chat.completions.create(
        model="TheBloke/dolphin-2.2.1-mistral-7B-GGUF",
        messages= history,
        temperature=0.7,
      )

      response = completion.choices[0].message.content
      history.append( {"role": "assistant", "content": response})
      word_list = word_list+"\n"+response

    with open(save_path,"w") as f:
        f.write(word_list)

def main():
    wlgen("akash.txt","akash_wordlist.txt",1)


if __name__== "__main__":
    main()

