import React,{useState} from 'react';
import { Link } from 'react-router-dom';
import loginimg from '../assets/login2.jpg';
import axios from "axios";

const Login = () => {

  const [username, setUsername] = useState('');
  const [password, setPass] = useState('');

  const handleLogin = async () => {
    console.log('User logged out');
    try {
      const postData = { username, password }; // Updated: Create an object to send in the POST request
      const response = await axios.post('http://127.0.0.1:8000/api/login/', postData);
      console.log(response.data);
      
    } catch (error) {
      console.log('Login Failed', error);
    }
  };

  const handleUsernameChange = (e) => {
    setUsername(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPass(e.target.value);
  };

return (
  <div className="flex h-screen bg-gray-200">
    <div className="w-1/2 bg-cover bg-center hidden md:block" style={{ backgroundImage: `url(${loginimg})` }}></div>
    <div className="w-full md:w-1/2 bg-white p-8 flex items-center justify-center">
      <div className="max-w-md w-full">
        <h2 className="text-3xl font-semibold text-gray-800 mb-6 text-center">Login</h2>
        <form className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="username">
              Username
            </label>
            <input
              className="border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="username"
              type="text"
              placeholder="Enter your username"
              onChange={handleUsernameChange}
            />
          </div>
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="password">
              Password
            </label>
            <input
              className="border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="password"
              type="password"
              placeholder="Enter your password"
              onChange={handlePasswordChange}
            />
          </div>
          <div className="mb-6 text-center">
            {/* Use Link instead of button and provide the 'to' prop with the desired route */}
            <Link
              to="/DashboardPage"
              className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
              onClick={handleLogin}
            >
              Sign In
            </Link>
          </div>
          <p className="text-center text-gray-600 text-sm">
            Forgot your password?{' '}
            <a className="text-blue-500 hover:text-blue-800" href="/DashboardPage">
              Reset Password
            </a>
          </p>
        </form>
        <p className="text-center text-gray-500 text-xs">&copy; 2024 Hyperloop Hackers. All rights reserved.</p>
      </div>
    </div>
  </div>
);
};

export default Login;
