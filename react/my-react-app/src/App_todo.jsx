import React, { useState, useEffect } from 'react';

// 할 일 항목 하나를 표시하는 컴포넌트
function TodoItem({ todo, onDelete }) {
  return (
    <div style={{ display: 'flex', justifyContent: 'space-between', padding: '10px', borderBottom: '1px solid #eee' }}>
      <span>{todo.text}</span>
      <button
        onClick={() => onDelete(todo.id)}
        style={{ background: 'red', color: 'white', border: 'none', padding: '5px 10px', cursor: 'pointer' }}
      >
        삭제
      </button>
    </div>
  );
}

// 메인 컴포넌트 (투두 리스트 앱)
function App() {
  // 1. 상태(State) 정의
  // todos: 할 일 목록 배열. 초기값은 빈 배열 []
  // newTodo: 새로 입력할 할 일 텍스트. 초기값은 빈 문자열 ''
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState('');

  // ⭐️ useEffect 훅 추가 ⭐️
  // 두 번째 인자([newTodo])에 배열로 상태를 넣어주면,
  // 해당 상태가 변경될 때마다 내부 코드가 실행됩니다.
  useEffect(() => {
    // 이 코드는 newTodo 상태가 완전히 업데이트된 후에 실행됨
    console.log("⭐️ newTodo 상태가 업데이트됨:", newTodo);
  }, [newTodo]); // 의존성 배열(dependency array)

  // 2. 할 일 추가 함수 (이벤트 핸들러)
  const handleAddTodo = () => {
    if (newTodo.trim() === '') return; // 빈 값은 추가하지 않음

    const newId = Date.now(); // 고유 ID 생성 (간단하게 현재 시간 사용)
    const newTodoItem = {
      id: newId,
      text: newTodo.trim(),
    };

    // 기존 todos 배열에 새 항목을 추가하여 상태 업데이트
    // ...todos : 기존 배열의 모든 항목을 복사
    setTodos([...todos, newTodoItem]);

    // 입력 필드 초기화
    setNewTodo('');
  };

  // 3. 할 일 삭제 함수
  const handleDeleteTodo = (id) => {
    // filter를 사용하여 삭제할 ID와 일치하지 않는 항목들만 남김
    const updatedTodos = todos.filter(todo => todo.id !== id);
    setTodos(updatedTodos); // 새로운 배열로 상태 업데이트
  };

  return (
    <div style={{ maxWidth: '400px', margin: '50px auto', border: '1px solid #ccc', padding: '20px' }}>
      <h1>간단 투두 리스트</h1>

      {/* 할 일 입력 섹션 */}
      <div style={{ display: 'flex', gap: '10px', marginBottom: '20px' }}>
        <input
          type="text"
          value={newTodo}
          onChange={(e) => setNewTodo(e.target.value)} // 입력 값 변경 시 newTodo 상태 업데이트
          placeholder="새 할 일을 입력하세요"
          style={{ flexGrow: 1, padding: '10px' }}
        />
        <button
          onClick={handleAddTodo}
          style={{ padding: '10px 15px' }}
        >
          추가
        </button>
      </div>

      {/* 할 일 목록 섹션 */}
      <div>
        {/* todos 배열을 순회하며 각 항목마다 TodoItem 컴포넌트 렌더링 */}
        {todos.map(todo => (
          <TodoItem
            key={todo.id}
            todo={todo}
            onDelete={handleDeleteTodo} // TodoItem에 삭제 함수를 속성(Props)으로 전달
          />
        ))}
      </div>

      {todos.length === 0 && <p style={{ textAlign: 'center', color: '#888' }}>아직 할 일이 없습니다!</p>}

    </div>
  );
}

export default App;