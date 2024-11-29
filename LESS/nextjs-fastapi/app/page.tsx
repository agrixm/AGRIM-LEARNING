"use client"
import { useState } from "react";

export default function ProfilePicPage() {
  const [username, setUsername] = useState("");
  const [profilePicUrl, setProfilePicUrl] = useState("");

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    const response = await fetch("/api/py/profile-pic", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ username }),
    });
    const data = await response.json();
    setProfilePicUrl(data.profile_pic_url);
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Get Instagram Profile Picture</h1>
      <form onSubmit={handleSubmit} className="mb-4">
        <label className="block mb-2">
          Username:
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            className="border p-2 text-black w-full"
            required
          />
        </label>
        <button type="submit" className="bg-blue-500 text-white p-2 mt-2">
          Get Profile Picture
        </button>
      </form>
      {profilePicUrl && (
        <div>
          <h2 className="text-xl font-bold mb-2">Profile Picture:</h2>
          <img src={profilePicUrl} alt="Profile" className="border p-2" />
        </div>
      )}
    </div>
  );
}