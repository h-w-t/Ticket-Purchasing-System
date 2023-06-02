import axios from 'axios';

axios.defaults.baseURL = 'http://127.0.0.1:8000/api/';
// axios.defaults.headers.common['Authorization'] = 'JWT token';

// 登录api
export interface LoginReq {
  username: string;
  password: string; 
}

export function login(data: LoginReq) {
  debugger
  return axios.post('/api/login', data)
    .then(res => res.data);
}