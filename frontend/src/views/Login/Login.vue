<template>
   <head>
      <title>登录</title>
   </head>
   <body>
      <form>
         <h1>Login</h1>
         <input type="text" placeholder="用户名" required=true />
         <input type="password" placeholder="密码" required=true />
         <button type="submit">&gt;&gt;&gt;登录&lt;&lt;&lt;</button>
      </form>
   </body>
</template>

<script setup lang='ts'>
</script>

<style scoped>
*{
    outline: none;
    user-select: none;
}

body{
    margin: 0;
    padding: 0;
    background: url(@assets/images/background.jpg);
    background-size: cover;
    background-position: center;
}

form{
    background-color: rgba(248, 248, 255, 0.3);
    width: 400px;
    height: 400px;
    border-radius: 30px;

    position: absolute;  
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);  


    backdrop-filter: blur(5px);
    border: 2px solid rgba(255,255,255, 0.3);
    border-top: 2px solid rgba(255,255,255, 0.5);
    box-shadow: 2px 2px 10px rgba(0,0,0, 0.2);
    text-align: center;
}

h1{
   margin: 20px;

   font-weight: xx-large;
   font-size: 64px;
   font-family: 'Microsoft YaHei';

   color: rgb(255, 255, 255);
   text-shadow: 2px 2px 4px rgba(0,0,0, 0.2);
   opacity: 0.9;
}

input{
   border: none;
   width: 88%;
   font-size: 22px;
   padding: 10px ;
   margin-bottom: 32px;
   border-radius: 16px;
   background-color: transparent;

   backdrop-filter: blur(5px);
   border-left: 2px solid rgba(255,255,255, 0.5);
   border-top: 2px solid rgba(255,255,255, 0.5);
   box-shadow: 2px 2px 10px rgba(0,0,0, 0.2);

   text-shadow: 2px 2px 2px rgba(0,0,0, 0.2);
   font-family: 'Microsoft YaHei';
   text-align: center;
   color: ghostwhite;
}

input.placeholder{
   color: rgba(ghostwhite, 1);
   opacity: 0.8;
}

button{
   width:240px;
   font-size: 24px;
   font-weight: bold;
   margin-top: 10px;
   cursor:pinter;

   border: none;
   padding: 10px ;
   margin-bottom: 32px;
   border-radius: 16px;
   background-color: rgba(255, 255, 255, 0.352);

   backdrop-filter: blur(5px);
   border-left: 2px solid rgba(255,255,255, 0.5);
   border-top: 2px solid rgba(255,255,255, 0.5);
   box-shadow: 2px 2px 10px rgba(0,0,0, 0.2);
}

button:hover{
   transition: 0.2s;
   background-color: rgba(255, 255, 255, 0.452);
   box-shadow: 2px 2px 10px rgba(0,0,0, 0.4);
}

input:focus{
   border:none;
   background-color: rgaba(black,0.1);
   text-shadow: 1px,1px,2px,rgba(255,255,255,0.2);
   border-right: 2px solid rgba(255,255,255, 0.3);
   border-bottom: 2px solid rgba(255,255,255, 0.3);   
   box-shadow: inset 2px 2px 2px rgba(0,0,0, 0.2);
}
</style>