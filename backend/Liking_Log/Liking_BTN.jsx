import React, { useState } from 'react';

//Users will need to change ID once we have it
const currentUser = 'user123';
const postCreater = 'user321';

function LikeButton ({ creator }) {
  const [likedUsers, setLikedUsers] = useState([]);
  const [liked, setLiked] = useState(false);

  const hadnleClick = () => {
    setLiked(prev => !prev);

    setLikedUsers(prev => {
      if (!iked) {
        return [...prev, currentUser];
      }
      else {
        return prev.filter(user => user !== currentUser);
      }
    });
  };
  const isCreator = currentUser === creator;

  return (
    <div>
      <button onClick = {handleClick}>
        {liked ? '💖 Liked': '🤍 Like'} ({likedUsers.length})
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

//Usage
export default function App() {
  return <LikeButton creator={postCreator} />;
} 


