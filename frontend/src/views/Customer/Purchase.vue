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
                  </el-icon>航班查询
                </template>
                <el-menu-item-group>
                  <el-menu-item index="1-1">按航班号查询</el-menu-item>
                  <el-menu-item index="1-2">按航空公司查询</el-menu-item>
                  <el-menu-item index="1-3">按出发地&目的地查询</el-menu-item>
                </el-menu-item-group>
              </el-sub-menu>
              <!-- 菜单栏2 -->
              <el-sub-menu index="2">
                <template #title>
                  <el-icon><icon-menu /></el-icon>机票预订
                </template>
                <el-menu-item-group>
                  <el-menu-item index="2-1">机票预定</el-menu-item>
                  <el-menu-item index="2-2">机票改签</el-menu-item>
                  <el-menu-item index="2-3">机票退订</el-menu-item>
                </el-menu-item-group>
              </el-sub-menu>
              <!-- 菜单栏3 -->
              <el-sub-menu index="3">
                <template #title>
                  <el-icon>
                    <setting />
                  </el-icon>用户中心
                </template>
                <el-menu-item-group>
                  <el-menu-item index="3-1">我</el-menu-item>
                  <el-menu-item index="3-2">我的订单</el-menu-item>
                  <el-menu-item index="3-3">帮助</el-menu-item>
                </el-menu-item-group>
              </el-sub-menu>
            </el-menu>
          </el-scrollbar>
        </el-aside>
  
        <el-container>
          <!-- 顶部状态栏 -->
          <el-header style="text-align: center; font-size: 28px;padding: 8px; margin-top: 5px;font-weight: bold;">
            🌐🌐🌐机票预订系统🌐🌐🌐
          </el-header>
          <!-- 主体内容 -->
          <el-main>
            <!-- <el-scrollbar> -->
              <!-- <template> -->
                <el-table :data="tableData" align="center">
                  <el-table-column prop="Flight_num" label="航班号" />
                  <el-table-column prop="Flight_co" label="航空公司" />
                  <el-table-column prop="From" label="出发地"/>
                  <el-table-column prop="Destination" label="目的地"  />
                  <el-table-column prop="Departure_time" label="起飞时间"/>
                  <el-table-column prop="Arrive_time" label="抵达时间"/>
                  <el-table-column prop="aero_type" label="飞机型号"/>
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
  
  interface Flights {
    Flight_num: string
    Flight_co: string
    From: string
    Destination: string
    Departure_time: string
    Arrive_time: string
    aero_type: string
  }
  
  const tableRowClassName = ({
    row,
    rowIndex,
  }: {
    row: Flights
    rowIndex: number
  }) => {
    if (rowIndex === 1) {
      return 'warning-row'
    } else if (rowIndex === 3) {
      return 'success-row'
    }
    return ''
  }
  
  const tableData: Flights[] = [
    {
      Flight_num: 'MU5138',
      Flight_co: '中国东方航空公司',
      From: '上海浦东国际机场',
      Destination: '北京大兴国际机场',
      Departure_time: '31/05/2023 12:00:00',
      Arrive_time: '31/05/2023 14:00:00',
      aero_type: 'B737'
    },
    {
      Flight_num: 'MU5138',
      Flight_co: '中国东方航空公司',
      From: '上海浦东国际机场',
      Destination: '北京大兴国际机场',
      Departure_time: '31/05/2023 12:00:00',
      Arrive_time: '31/05/2023 14:00:00',
      aero_type: 'B737'
    },
    {
      Flight_num: 'MU5138',
      Flight_co: '中国东方航空公司',
      From: '上海浦东国际机场',
      Destination: '北京大兴国际机场',
      Departure_time: '31/05/2023 12:00:00',
      Arrive_time: '31/05/2023 14:00:00',
      aero_type: 'B737'
    },
    {
      Flight_num: 'MU5138',
      Flight_co: '中国东方航空公司',
      From: '上海浦东国际机场',
      Destination: '北京大兴国际机场',
      Departure_time: '31/05/2023 12:00:00',
      Arrive_time: '31/05/2023 14:00:00',
      aero_type: 'B737'
    },
    {
      Flight_num: 'MU5138',
      Flight_co: '中国东方航空公司',
      From: '上海浦东国际机场',
      Destination: '北京大兴国际机场',
      Departure_time: '31/05/2023 12:00:00',
      Arrive_time: '31/05/2023 14:00:00',
      aero_type: 'B737'
    },
    {
      Flight_num: 'MU5138',
      Flight_co: '中国东方航空公司',
      From: '上海浦东国际机场',
      Destination: '北京大兴国际机场',
      Departure_time: '31/05/2023 12:00:00',
      Arrive_time: '31/05/2023 14:00:00',
      aero_type: 'B737'
    },
    {
      Flight_num: 'MU5138',
      Flight_co: '中国东方航空公司',
      From: '上海浦东国际机场',
      Destination: '北京大兴国际机场',
      Departure_time: '31/05/2023 12:00:00',
      Arrive_time: '31/05/2023 14:00:00',
      aero_type: 'B737'
    },
    {
      Flight_num: 'MU5138',
      Flight_co: '中国东方航空公司',
      From: '上海浦东国际机场',
      Destination: '北京大兴国际机场',
      Departure_time: '31/05/2023 12:00:00',
      Arrive_time: '31/05/2023 14:00:00',
      aero_type: 'B737'
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