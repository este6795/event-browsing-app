import React, { useState } from 'react';

// Users will need to change ID once we have it
const currentUser = 'user123';
const postCreator = 'user321';

function LikeButton({ creator }) {
  // Use a single state to manage the liked users and infer the "liked" status from it.
  const [likedUsers, setLikedUsers] = useState([]);
  
  const liked = likedUsers.includes(currentUser);

  const handleClick = () => {
    setLikedUsers(prev => {
      // Check if the current user is already in the array.
      if (prev.includes(currentUser)) {
        // If so, filter them out (unlike).
        return prev.filter(user => user !== currentUser);
      } else {
        return [...prev, currentUser];
      }
    });
  };

  const isCreator = currentUser === creator;

  return (
    <div>
      <button onClick={handleClick}>
        {liked ? '👍 Liked' : '👍 Like'} ({likedUsers.length})
      </button>

      {isCreator && (
        <div style={{ marginTop: '10px' }}>
          <strong>Users who liked this:</strong>
          <ul>
            {likedUsers.map(user => (
              <li key={user}>{user}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

// Usage
export default function App() {
  return <LikeButton creator={postCreator} />;
}
