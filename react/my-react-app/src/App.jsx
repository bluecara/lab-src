import React, { useState } from 'react';

function App() {
  const [count, setCount] = useState(0);

  // 1. 증가 함수
  const handleIncrement = () => {
    setCount(prevCount => prevCount + 1);
  };

  // 2. 감소 함수
  const handleDecrement = () => {
    setCount(prevCount => prevCount - 1);
  };

  // 3. ⭐️ 초기화 함수 추가 ⭐️
  const handleReset = () => {
    // setCount에 초기 상태 값(0)을 직접 전달하여 상태를 재설정합니다.
    setCount(0);
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '100px', fontFamily: 'Arial' }}>
      <h1>간단 카운터 앱</h1>

      {/* 상태 값 표시 */}
      <p style={{ fontSize: '72px', margin: '20px 0' }}>
        {count}
      </p>

      <div style={{ display: 'flex', gap: '20px', justifyContent: 'center' }}>
        <button
          onClick={handleDecrement}
          style={{ padding: '15px 30px', fontSize: '24px', cursor: 'pointer', backgroundColor: '#f44336', color: 'white', border: 'none', borderRadius: '5px' }}
        >
          - 감소
        </button>

        {/* 4. ⭐️ 초기화 버튼 추가 ⭐️ */}
        <button
          onClick={handleReset} // 버튼 클릭 시 handleReset 함수 실행
          style={{ padding: '15px 30px', fontSize: '24px', cursor: 'pointer', backgroundColor: '#ff9800', color: 'white', border: 'none', borderRadius: '5px' }}
        >
          ♻️ 초기화
        </button>

        <button
          onClick={handleIncrement}
          style={{ padding: '15px 30px', fontSize: '24px', cursor: 'pointer', backgroundColor: '#4CAF50', color: 'white', border: 'none', borderRadius: '5px' }}
        >
          + 증가
        </button>
      </div>
    </div>
  );
}

export default App;