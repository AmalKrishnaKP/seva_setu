import axios from "axios";

export const api= axios.create({
    baseURL:"http://127.0.0.1:8000/seva_setu/v1",
    withCredentials: true,
    headers: { 'Content-Type': 'application/json' },

}

)