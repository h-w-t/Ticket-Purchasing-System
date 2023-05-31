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
                <el-icon>
                  <message />
                </el-icon>用户请求
              </template>
              <el-menu-item-group>
                <el-menu-item index="1-1">改签</el-menu-item>
                <el-menu-item index="1-2">退票</el-menu-item>
                <el-menu-item index="1-3">问讯</el-menu-item>
              </el-menu-item-group>
            </el-sub-menu>
            <!-- 菜单栏2 -->
            <el-sub-menu index="2">
              <template #title>
                <el-icon><icon-menu /></el-icon>航班管理
              </template>
              <el-menu-item-group>
                <el-menu-item index="2-1">添加航班</el-menu-item>
                <el-menu-item index="2-2">修改航班</el-menu-item>
                <el-menu-item index="2-3">删除航班</el-menu-item>
              </el-menu-item-group>
            </el-sub-menu>
            <!-- 菜单栏3 -->
            <el-sub-menu index="3">
              <template #title>
                <el-icon>
                  <setting />
                </el-icon>订单管理
              </template>
              <el-menu-item-group>
                <el-menu-item index="3-1">所有订单</el-menu-item>
                <el-menu-item index="3-2">机票退票</el-menu-item>
                <el-menu-item index="3-3">机票改签</el-menu-item>
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
          <!-- <el-scrollbar> -->
            <!-- <template> -->
              <el-table :data="tableData" align="center">
                <el-table-column prop="_Request_time" label="请求发起时间" width="200" />
                <el-table-column prop="_Request_user" label="请求用户" width="160" />
                <el-table-column prop="_Request_detail" label="请求内容"/>
                <el-table-column prop="_Request_status" label="状态" width="130" />
              </el-table>
            <!-- </template> -->
          <!-- </el-scrollbar> -->
        </el-main>
      </el-container>


    </div>
  </body>
</template>

<script setup lang='ts'>

import { ref } from 'vue'
import { Menu as IconMenu, Message, Setting } from '@element-plus/icons-vue'

interface Requests {
  _Request_time: string
  _Request_user: string
  _Request_detail: string
  _Request_status: string
}

const tableRowClassName = ({
  row,
  rowIndex,
}: {
  row: Requests
  rowIndex: number
}) => {
  if (rowIndex === 1) {
    return 'warning-row'
  } else if (rowIndex === 3) {
    return 'success-row'
  }
  return ''
}

const tableData: Requests[] = [
  {
    _Request_time: '31/05/2023 12:00:00',
    _Request_user: 'Tom',
    _Request_detail: 'I want to book a ticket from Beijing to Shanghai.',
    _Request_status: '已完成'
  },
  {
    _Request_time: '31/05/2023 12:00:00',
    _Request_user: 'Steve',
    _Request_detail: 'I want to book a ticket from Beijing to Shanghai.',
    _Request_status: '待处理'
  },
  {
    _Request_time: '31/05/2023 12:00:00',
    _Request_user: 'Smith',
    _Request_detail: 'I want to book a ticket from Beijing to Shanghai.',
    _Request_status: '已完成'
  },
  {
    _Request_time: '31/05/2023 12:00:00',
    _Request_user: 'John',
    _Request_detail: 'I want to book a ticket from Beijing to Shanghai.',
    _Request_status: '已完成'
  },
  {
    _Request_time: '31/05/2023 12:00:00',
    _Request_user: 'Tom',
    _Request_detail: 'I want to book a ticket from Beijing to Shanghai.',
    _Request_status: '已完成'
  },
  {
    _Request_time: '31/05/2023 12:00:00',
    _Request_user: 'Steve',
    _Request_detail: 'I want to book a ticket from Beijing to Shanghai.',
    _Request_status: '待处理'
  },
  {
    _Request_time: '31/05/2023 12:00:00',
    _Request_user: 'Smith',
    _Request_detail: 'I want to book a ticket from Beijing to Shanghai.',
    _Request_status: '已完成'
  },
  {
    _Request_time: '31/05/2023 12:00:00',
    _Request_user: 'John',
    _Request_detail: 'I want to book a ticket from Beijing to Shanghai.',
    _Request_status: '已完成'
  },
]

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
  border-radius: 20px;
  margin: 10px 0 5px 5px;
}

.el-menu {
  border-right: none;
  background: rgba(255, 255, 255, 0.4);
  border-radius: 20px;
}

.el-menu .el-menu-item{
  background: rgba(255, 255, 255, 0);
}

.el-main {
  padding: 0 5px 10px 5px;
  background: transparent;
}

/* .el-scrollbar {
  background: transparent;
  overflow: hidden;
} */

.el-table {
  border-radius:15px;
  height: 100%;
  background: rgba(255, 255, 255, 0.4);
}

.el-table .warning-row {
  --el-table-tr-bg-color: var(--el-color-warning-light-9);
}
.el-table .success-row {
  --el-table-tr-bg-color: var(--el-color-success-light-9);
}

</style>