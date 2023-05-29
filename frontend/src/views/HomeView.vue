<template>
    <head>
        <title>Home</title>
   </head>
   <body>
        <h1 class="welcome">🛬&nbsp;机票订购系统&nbsp;🛫</h1>
        <nav class="navigator">
            <router-link to="/login">登录</router-link>&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
            <router-link to="/sign-up">注册</router-link>
        </nav>
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
    position: relative;
}
.welcome{
    color: antiquewhite;
    text-align: center;
    font-size: 64px;
    text-shadow: 2px 2px 4px rgba(0,0,0, 0.2);
    opacity: 0.9;

    position: fixed;
    top: 35%;
    left: 50%;
    transform: translate(-50%, -50%);
}

.navigator {
    color: antiquewhite;
    text-decoration: none;
    font-family: 'Microsoft YaHei';
    text-align: center;
    font-size: 32px;
    text-shadow: 2px 2px 2px rgba(0,0,0, 0.2);
    opacity: 0.9;

    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

a{
    color: antiquewhite;
    text-decoration: none;
}

a:hover{
    color: rgba(219, 142, 255, 0.629);
    text-shadow: 2px 2px 4px rgba(0,0,0, 0.2);
    opacity: 0.9;
    background-color: rgba(254, 215, 255, 0.37);
    border-radius: 5px;
}
</style>
