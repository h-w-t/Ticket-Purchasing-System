<template>
  <head>
    <title>后台系统</title>
  </head>

  <body>
    <div class="mainwindow">
      
      <el-aside width="20%" class="aside">
        <el-scrollbar>
          <el-menu :default-openeds="['1']">
            <!-- 菜单栏1 -->
            <el-sub-menu index="1">
              <template #title>
                <el-icon><message /></el-icon>用户请求
              </template>
              <el-menu-item-group>
                <el-menu-item index="1-1">Option 1</el-menu-item>
                <el-menu-item index="1-2">Option 2</el-menu-item>
                <el-menu-item index="1-3">Option 3</el-menu-item>
              </el-menu-item-group>             
            </el-sub-menu>
            <!-- 菜单栏2 -->
            <el-sub-menu index="2">
              <template #title>
                <el-icon><icon-menu /></el-icon>航班管理
              </template>
              <el-menu-item-group>
                <el-menu-item index="2-1">Option 1</el-menu-item>
                <el-menu-item index="2-2">Option 2</el-menu-item>
                <el-menu-item index="2-3">Option 3</el-menu-item>
              </el-menu-item-group>
            </el-sub-menu>
            <!-- 菜单栏3 -->
            <el-sub-menu index="3">
              <template #title>
                <el-icon><setting /></el-icon>订单管理
              </template>
              <el-menu-item-group>
                <el-menu-item index="3-1">Option 1</el-menu-item>
                <el-menu-item index="3-2">Option 2</el-menu-item>
                <el-menu-item index="3-3">Option 3</el-menu-item>
              </el-menu-item-group>
            </el-sub-menu>
          </el-menu>
        </el-scrollbar>
      </el-aside>

      <el-container>
        <!-- 顶部状态栏 -->
        <el-header style="text-align: center; font-size: 28px;padding: 8px; margin-top: 5px;font-weight: bold;">
          ⚙️机票预定后台管理系统⚙️
        </el-header>
        <!-- 主体内容 -->
        <el-main>
          <el-scrollbar style="overflow: hidden;"> 
            <el-table :data="tableData" height="100%">
              <el-table-column prop="_Request_time" label="Request time" width="200" />
              <el-table-column prop="_Request_user" label="Request user" width="140" />
              <el-table-column prop="_Request_detail" label="Request_detail" width="400"/>
              <el-table-column prop="_Request_status" label="Request status" width="130"/>
            </el-table>
          </el-scrollbar>
        </el-main>
      </el-container>


    </div>
  </body>
</template>

<script setup lang='ts'>

import { ref } from 'vue'
import { Menu as IconMenu, Message, Setting } from '@element-plus/icons-vue'

const item = {
  _Request_time: '31/05/2023 12:00:00',
  _Request_user: 'Tom',
  _Request_detail: 'I want to book a ticket from Beijing to Shanghai.',
  _Request_status: '已完成'
}
const tableData = ref(Array.from({ length: 20 }).fill(item))

</script>

<style scoped>
* {
  outline: none;
  user-select: none;
}

body {
  background: url(@assets/images/background.jpg);
  background-size: cover;
  background-position: center;
  margin: 0;
  padding: 0;
}

.mainwindow {
  background-color: rgba(248, 248, 255, 0.3);
  width: 80%;
  height: 80%;
  border-radius: 30px;

  display: flex;
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

.aside {
  color: var(--el-text-color-primary);
  background: transparent;
  border-right: none;
  border-radius: 30px;
}

.el-menu {
  border-right: none;
  background: rgba(255, 255, 255, 0.4);
  border-radius: 15px;
}


.el-main {
  padding: 0 0 0 5px;
  background: transparent;
  border-bottom-right-radius: 30px;
}

.el-scrollbar {
  background: transparent;
  overflow: hidden;
}

.el-table {
  border-top-left-radius: 15px;
  border-bottom-left-radius: 15px;
  height: 100%;
}

/* ::v-deep{
  .el-table__header-wrapper {
    border-top-left-radius: 15px;
    border-top-right-radius: 15px;
  }
  .el-table__body-wrapper {
    border-bottom-left-radius: 15px;
    border-bottom-right-radius: 15px;
  }
} */

</style>