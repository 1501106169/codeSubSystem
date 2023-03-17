
import axios from 'axios'

const http = axios.create({
    baseURL: 'http://192.168.81.128:80',
    timeout: 10000,
})

export default http;