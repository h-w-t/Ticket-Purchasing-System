<template>
   <head>
      <title>登录</title>
   </head>

   <body>
      <!-- <form @submit.prevent="handleSubmit"> -->
      <form>
         <h1>Login</h1>
         <input type="text" placeholder="用户名" required=true  v-model="LoginParams.username"/>
         <input type="password" placeholder="密码" required=true  show-password:true v-model="LoginParams.password"/>
         <button type="submit" @click="onSubmit">&gt;&gt;&gt;登录&lt;&lt;&lt;</button>
      </form>
   </body>
</template>

<script setup lang='ts'>
import type { LoginReq } from '@/api';
import {login} from '@/api';
import { reactive } from 'vue';
import { useRouter } from 'vue-router';
import { useField, useForm } from 'vee-validate';
import { required } from '@vee-validate/rules';
import axios from 'axios';

const LoginParams : LoginReq = reactive({
   username: '',
   password: '',
});

//表单验证
// const { handleSubmit } = useForm();

// const { value: username, errorMessage: usernameError } = useField('LoginParams.username', required);
// const { value: password, errorMessage: passwordError } = useField('LoginParams.password', required);

// const errors = {
//   username: usernameError,
//   password: passwordError,
// };

// 跳转无法实现
function onSubmit(this: { $router: any, error: any, $message: any }) {
   // console.log('LoginParams:', LoginParams);
   // login(LoginParams)
   //    .then(res => {
   //       console.log('Response: ', res.data);
   //       if (LoginParams.username.startsWith('arp-')) {
   //          this.$router.push('/air-rep');
   //       } else if (LoginParams.username.startsWith('cst-')) {
   //          this.$router.push('/purchase');
   //       }
   //    })
   //    .catch(err => {
   //       this.error = err.response.data.message;
   //       this.$message.error(this.error);
   //    });
   if (LoginParams.username.startsWith('arp-')) {
            this.$router.push('/air-rep');
         } else if (LoginParams.username.startsWith('cst-')) {
            this.$router.push('/purchase');
         }
}

// }
function getTargetRoute(username: string) {
   if (username.startsWith('arp-')) {
      return "/air-rep";
   } else if (username.startsWith('cst-')) {
      return "/purchase";
   }
}

</script>

<style scoped>
* {
   outline: none;
   user-select: none;
}

body {
   margin: 0;
   padding: 0;
   background: url(@assets/images/background.jpg);
   background-size: cover;
   background-position: center;
}

form {
   background-color: rgba(248, 248, 255, 0.3);
   width: 400px;
   height: 400px;
   border-radius: 30px;

   position: absolute;
   top: 50%;
   left: 50%;
   transform: translate(-50%, -50%);


   backdrop-filter: blur(5px);
   border: 2px solid rgba(255, 255, 255, 0.3);
   border-top: 2px solid rgba(255, 255, 255, 0.5);
   box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
   text-align: center;
}

h1 {
   margin: 20px;

   font-weight: xx-large;
   font-size: 64px;
   font-family: 'Microsoft YaHei';

   color: rgb(255, 255, 255);
   text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
   opacity: 0.9;
}

input {
   border: none;
   width: 88%;
   font-size: 22px;
   padding: 10px;
   margin-bottom: 32px;
   border-radius: 16px;
   background-color: transparent;

   backdrop-filter: blur(5px);
   border-left: 2px solid rgba(255, 255, 255, 0.5);
   border-top: 2px solid rgba(255, 255, 255, 0.5);
   box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);

   text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.2);
   font-family: 'Microsoft YaHei';
   text-align: center;
   color: ghostwhite;
}

input.placeholder {
   color: rgba(ghostwhite, 1);
   opacity: 0.8;
}

button {
   width: 240px;
   font-size: 24px;
   font-weight: bold;
   margin-top: 10px;
   cursor: pinter;

   border: none;
   padding: 10px;
   margin-bottom: 32px;
   border-radius: 16px;
   background-color: rgba(255, 255, 255, 0.352);

   backdrop-filter: blur(5px);
   border-left: 2px solid rgba(255, 255, 255, 0.5);
   border-top: 2px solid rgba(255, 255, 255, 0.5);
   box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
}

button:hover {
   transition: 0.2s;
   background-color: rgba(255, 255, 255, 0.452);
   box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.4);
}

input:focus {
   border: none;
   background-color: rgaba(black, 0.1);
   text-shadow: 1px, 1px, 2px, rgba(255, 255, 255, 0.2);
   border-right: 2px solid rgba(255, 255, 255, 0.3);
   border-bottom: 2px solid rgba(255, 255, 255, 0.3);
   box-shadow: inset 2px 2px 2px rgba(0, 0, 0, 0.2);
}
</style>