import React, { useState } from 'react';

function LikeButton() {
  const [liked, setLiked] = useState(false);
  const [likes, setLikes] = useState(0);

  const handleClick = () => {
    if (liked) {
      setLikes(prev => Math.max(prev - 1, 0));
    }
    else {
      setLikes(prev => + 1);
    }
    setLiked(prev => !prev);
  };

  return (
    <button onClick = {handleClick} style = {{ fontSize: '18px', padding: '10px 20px'}}>
    </button>
  );
}
export default LikeButton; 
