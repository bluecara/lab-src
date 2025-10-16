import React, { useState, useEffect } from 'react';

// ----------------------------------------------------
// 1. 디스플레이 컴포넌트
// ----------------------------------------------------
function CalculatorDisplay({ value }) {
  return (
    <div style={{
      backgroundColor: '#222',
      color: 'white',
      fontSize: '48px',
      padding: '20px',
      textAlign: 'right',
      borderRadius: '5px 5px 0 0',
      marginBottom: '10px'
    }}>
      {value}
    </div>
  );
}

// ----------------------------------------------------
// 2. 버튼 컴포넌트
// ----------------------------------------------------
function CalculatorButton({ label, onClick, style = {} }) {
  return (
    <button
      onClick={() => onClick(label)}
      style={{
        ...style,
        width: '100%',
        height: '80px',
        fontSize: '24px',
        cursor: 'pointer',
        border: '1px solid #333',
        borderRadius: '5px',
        backgroundColor: label === '=' ? '#ff9500' : (isNaN(label) ? '#bbb' : '#e0e0e0'),
        color: label === '=' ? 'white' : 'black',
      }}
    >
      {label}
    </button>
  );
}


// ----------------------------------------------------
// 3. 메인 앱 컴포넌트
// ----------------------------------------------------
function App() {
  // ⭐️ 핵심 상태 ⭐️
  const [displayValue, setDisplayValue] = useState('0'); // 화면에 표시되는 값
  const [operator, setOperator] = useState(null); // 현재 선택된 연산자 (+, -, *, /)
  const [firstValue, setFirstValue] = useState(null); // 첫 번째 숫자 값
  const [waitingForSecondValue, setWaitingForSecondValue] = useState(false); // 두 번째 값 입력을 기다리는지 여부

  useEffect(() => {
    //console.log("displayValue : ", displayValue);
  }, [displayValue]);

  // 버튼 클릭 시 호출되는 메인 함수
  const handleButtonClick = (buttonLabel) => {
    //console.log(">> ", buttonLabel);

    // 1. 숫자 처리
    if (!isNaN(buttonLabel) || buttonLabel === '.') {
      handleNumber(buttonLabel);
    }
    // 2. 연산자 처리
    else if (['+', '-', '×', '÷', '%'].includes(buttonLabel)) {
      handleOperator(buttonLabel);
    }
    // 3. 등호 (=) 처리
    else if (buttonLabel === '=') {
      handleEqual();
    }
    // 4. 초기화 (C) 처리
    else if (buttonLabel === 'C') {
      handleClear();
    }
  };

  // ⭐️ 숫자 입력 처리 ⭐️
  const handleNumber = (number) => {
    console.log("number : ", number, " / displayValue : ", displayValue, " / waitingForSecondValue : ", waitingForSecondValue);

    // 두 번째 값 입력을 기다리고 있으면 (연산자 입력 직후) 화면을 초기화
    if (waitingForSecondValue) {
      setDisplayValue(number);
      setWaitingForSecondValue(false);
    } else {
      // '0' 상태일 때는 덮어쓰고, 아니면 기존 값에 추가
      setDisplayValue(displayValue === '0' || displayValue === '00' ? number.replace('00', '0') : displayValue + number);
    }
  };

  // ⭐️ 연산자 처리 ⭐️
  const handleOperator = (nextOperator) => {
    const inputValue = parseFloat(displayValue);

    // 첫 번째 입력이 아니거나, 이미 연산자가 선택되어 있으면 계산부터 실행
    if (firstValue !== null && operator && !waitingForSecondValue) {
      const result = performCalculation();
      setFirstValue(result);
      setDisplayValue(String(result));
    } else if (operator === null) {
      setFirstValue(inputValue);
    }

    setWaitingForSecondValue(true);
    setOperator(nextOperator);
  };

  // ⭐️ 등호 (=) 처리 ⭐️
  const handleEqual = () => {
    if (firstValue === null || operator === null) return;

    const result = performCalculation(true); // 최종 계산
    setDisplayValue(String(result));
    setFirstValue(null); // 계산 후 상태 초기화
    setOperator(null);
    setWaitingForSecondValue(false);
  };

  // ⭐️ 초기화 (C) 처리 ⭐️
  const handleClear = () => {
    setDisplayValue('0');
    setOperator(null);
    setFirstValue(null);
    setWaitingForSecondValue(false);
  };

  // ⭐️ 실제 계산 로직 ⭐️
  const performCalculation = (isFinal = false) => {
    const currentValue = parseFloat(displayValue);
    const prevValue = firstValue;

    // 간단한 사칙연산
    if (operator === '+') return prevValue + currentValue;
    if (operator === '-') return prevValue - currentValue;
    if (operator === '×') return prevValue * currentValue;
    if (operator === '÷') return prevValue / currentValue;
    if (operator === '%') return prevValue % currentValue;

    // 최종 등호 계산이 아닐 때는 현재 값 반환
    return currentValue;
  };

  // 버튼 레이아웃 정의
  const buttons = [
    'C', '%', '÷', '×',
    '7', '8', '9', '-',
    '4', '5', '6', '+',
    '1', '2', '3', '.',
    '00', '0', '='
  ];

  return (
    <div style={{ maxWidth: '320px', margin: '50px auto', boxShadow: '0 4px 8px rgba(0,0,0,0.1)' }}>
      {/* 디스플레이 */}
      <CalculatorDisplay value={displayValue} />

      {/* 버튼 그리드 */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(4, 1fr)',
        gap: '1px',
        padding: '1px',
        backgroundColor: '#333'
      }}>
        {buttons.map((label) => (
          <CalculatorButton
            key={label}
            label={label}
            onClick={handleButtonClick}
            // = 버튼은 두 칸을 차지하도록 스타일 적용
            style={label === '=' ? { gridColumn: 'span 2' } : {}}
          />
        ))}
      </div>
    </div>
  );
}

export default App;