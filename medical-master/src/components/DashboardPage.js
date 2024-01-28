// DashboardPage.js

import React, { useState } from 'react';

const SampleUser = ({ user }) => {
  return (
    <div className="mt-8">
      <h3 className="text-xl font-semibold mb-4">Sample User Details</h3>
      <div className="grid grid-cols-2 gap-4">
        <div>
          <label className="block text-gray-700 text-sm font-bold mt-4">Username:</label>
          <p className="text-gray-700">{user.username}</p>
        </div>
        <div>
          <label className="block text-gray-700 text-sm font-bold mt-4">Email:</label>
          <p className="text-gray-700">{user.email}</p>
        </div>
      </div>
    </div>
  );
};

const DashboardPage = () => {
  const [selectedUserType, setSelectedUserType] = useState('new');
  const [searchQuery, setSearchQuery] = useState('');

  const handleSearchInputChange = (event) => {
    setSearchQuery(event.target.value);
  };

  const handleSearch = () => {
    console.log('Searching for:', searchQuery);
  };

  const handleUserTypeChange = (event) => {
    setSelectedUserType(event.target.value);
  };

  const handleLogout = () => {
    console.log('User logged out');
  };

  const sampleUser = [
    { username: 'JohnDoe', email: 'john.doe@example.com' },
    { username: 'JohnDoe', email: 'john.doe@example.com' },
    { username: 'JohnDoe', email: 'john.doe@example.com' },
  ];

  return (
    <div className="h-screen flex flex-col bg-gray-100">
      {/* Navigation Bar */}
      <nav className="bg-blue-500 p-4 text-white">
        <div className="flex justify-between items-center">
          <div className="text-lg font-semibold">Clinic Dashboard</div>
          <button onClick={handleLogout} className="hover:underline cursor-pointer">
            Logout
          </button>
        </div>
      </nav>

      {/* Main Content */}
      <div className="flex-1 p-8 flex">
        {/* User Type Dropdowns - Full Width */}
        <div className="flex-1 bg-white rounded-lg p-8 shadow-md">
          <h2 className="text-3xl font-semibold text-gray-800 mb-6">Dashboard</h2>
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="userType">
              Select User Type:
            </label>
            <div className="flex">
              <select
                className="w-full border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                id="userType"
                value={selectedUserType}
                onChange={handleUserTypeChange}
              >
                <option value="new">New User</option>
                <option value="old">Existing User</option>
              </select>
            </div>
          </div>

          {/* Conditional Rendering based on selectedUserType */}
          {selectedUserType === 'new' && (
            <div>
              {/* Render New User Form */}
              <h3 className="text-xl font-semibold mb-4">New User Form</h3>
              {/* Form fields for new users */}
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="block text-gray-700 text-sm font-bold mt-4" htmlFor="username">
                    Username:
                  </label>
                  <input
                    className="border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    id="username"
                    type="text"
                    placeholder="Enter username"
                  />
                </div>
                <div>
                  <label className="block text-gray-700 text-sm font-bold mt-4" htmlFor="email">
                    Email:
                  </label>
                  <input
                    className="border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    id="email"
                    type="email"
                    placeholder="Enter email"
                  />
                </div>
              </div>
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="block text-gray-700 text-sm font-bold mt-4" htmlFor="usernameExisting">
                    PhoneNumber:
                  </label>
                  <input
                    className="border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    id="usernameExisting"
                    type="text"
                    placeholder="Enter PhoneNumber"
                  />
                </div>
                <div>
                  <label className="block text-gray-700 text-sm font-bold mt-4" htmlFor="uploadImageExisting">
                    Xray Image:
                  </label>
                  <input
                    className="border w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    id="uploadImageExisting"
                    type="file"
                  />
                </div>
              </div>
            </div>
          )}

          {selectedUserType === 'old' && (
            <div>
              {/* Render Existing User Form */}
              <h3 className="text-xl font-semibold mb-4">Existing User Form</h3>
              {/* Form fields for existing users */}
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="block text-gray-700 text-sm font-bold mt-4" htmlFor="usernameExisting">
                    Username:
                  </label>
                  <input
                    className="border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    id="usernameExisting"
                    type="text"
                    placeholder="Enter username"
                  />
                </div>
                <div>
                  <label className="block text-gray-700 text-sm font-bold mt-4" htmlFor="uploadImageExisting">
                    Xray Image:
                  </label>
                  <input
                    className="border w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    id="uploadImageExisting"
                    type="file"
                  />
                </div>
              </div>
            </div>
          )}

          {/* Search Section */}
          <div className="flex items-center mt-8">
            <input
              className="border rounded w-3/4 py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              type="text"
              placeholder="Search existing users..."
              value={searchQuery}
              onChange={handleSearchInputChange}
            />
            <button
              className="ml-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
              onClick={handleSearch}
            >
              Search
            </button>
          </div>

          {sampleUser.map((user, index) => (
            <SampleUser key={index} user={user} />
          ))}

        </div>
      </div>
    </div>
  );
};

export default DashboardPage;
