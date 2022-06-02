# Coding Conventions

### 1. Overview
* 협업을 중점으로 (쉽게 읽히는) 좋은 코드로 작성하기
* base on PSR : https://www.php-fig.org/psr/psr-2/
* https://developer.wordpress.org/coding-standards/wordpress-coding-standards/php/
<br><br>

### 2. Basic
* Common
    + 괄호, 쉼표, 공백 및 중괄호`{}`의 배치에 유의
    + 숫자로 시작 X
    + 약어 사용 X
    + 괄호 `()` 사이에 공백 X
    + 인수 목록 각 쉼표 앞에 공백 X, 쉼표 뒤에 공백 하나 O
        ```
        bar();
        bar(...['foo','bar']);
        $foo->bar($arg1);
        Foo::bar($arg2, $arg3);
        ```
* File
    + `<?php` / `<?=` 태그만 사용
    + PHP code만 존재 → `?>` 태그 생략
    + Type : Unix
    + Character Encoding : BOM이 없는 UTF-8
* Extension    
    |Kind|Extension|
    |---|:---:|
    |Default|*.html|
    |common|*.php|
    |include|*.inc.php|
    |ajax|*.ajax.php|
* Quotation Mark
    + HTML / Query / reqular expressions : 쌍타옴표 `"`
    + PHP code / Javascript : 홀따옴표 `'`
* Indenting
    + 4 space
    + tab 사용 X
* Naming
    + Class : `PascalCase`
        - ex) ClassName
    + Variable / Parameter : `camelCase`
        - ex) helloWorld
    + Method / Function : `camelCase` + 동사/전치사
        - ex) selectTable / countNumber / withUserId
    + Constant : `snake case`
        - ex) public $SET_NUMBER = 1;
    + 지역변수 / pirvate 변수 : under_score `_` 로 시작
        - ex) _privateVariableName = '';
    + under_score `_` 는 단어와 단어 조합할 때만 사용
        - ex) section_list
    + under_score `_` 가 포함된 약속어는 숫자, 영문 소문자와 조합하여 
        - ex) no1, no2
<br><br>

### 3. Class (클래스)
* 명사 사용
* `StudlyCaps` 규칙 사용
* under_score `_` 사용 X
* 여는 중괄호`{` , 닫는 중괄호`}` 는 **반드시** 다음줄에 명시
    - [x] Correct
    ```
    class ClassName extends ParentClass
    {
        // constants, properties, method
    }
    ```
    - [ ] Incorrect
    ```
    class ClassName extends ParentClass {
        // constants, properties, method
    }
    ```

    #### 3-1. Constants
    > + 모두 대문자와 under_score `_` 만으로 선언
    > + public, private, protect 위치 순서
    ```
    public $FOO = null;
    public static int $BAR = 0;
    ```

    #### 3-2. Methods & Functions
    > + 이름 다음에 공백 X
    > + 연산자 `&` 를 사용하면 뒤에 공백 X
    ```
    public funciton fooBarBaz($arg1, &$arg2, $arg3 = [], &...$arg4)
    {
        // method body
    }
    ```
    > + 인수 목록을 여러줄로 표시할 경우, 각 줄에 한 번 들여쓰기 추가
    ```
    public function aVeryLongMethodName(
        ClassTypeHint $arg1,
        &$arg2,
        array $arg3 = []
    ) {
        // method body
    }
    ```    
    > + abstract와 final 선언이 있을 경우, 가시성 선언 앞에 선언
    ```
    abstract class ClassName
    {
        protected static $foo;

        abstract protected function zim();

        final public static function bar()
        {
            // method body
        }
    }
    ```

    #### 3-3. Anonymous (익명)
    ```
    $instance = new class {};
    ```
<br>

### 4. Variable (변수)
* 임시 변수명
    + integer : i, j, k, m, n
    + character : c, d, e
<br><br>

### 5. Control (제어)
* 제어 구조 키워드 다음에 하나의 공백 O
* 닫는 괄호 `)` 와 여는 중괄호 `{` 사이에 하나의 공백 O
* 본문은 한 번 **들여쓰기** O
* 닫는 중괄호 `}` 는 몸체 뒤의 다음 줄 O
    #### 5-1. if, elseif, else
    ```
    if ($expr1) {
        // if body
    } elseif ($expr2) {
        // elseif body
    } elseif (($expr3) || ($expr4)) {
        // elseif body
    } else {
        // else body;
    }
    ```
    + 조건문이 2개 이상일 경우 여러줄로 표시
        ```
        if (
            $expr1
            && $expr2
        ) {
            // if body
        } elseif (
            $expr3
            && $expr4
        ) {
            // elseif body
        }
        ```
    
    #### 5-2. for, foreach
    ```
    for ($i = 0; $i < 10; $i++) {
        // for body
    }
    
    foreach ($iterable as $key => $value) {
        // foreach body
    }
    ```
    
    #### 5-3. while, do while
    ```
    while ($expr) {
        // structure body
    }
    
    while (
        $expr1
        && $expr2
    ) {
        // structure body
    }
    ```
    ```
    do {
        // structure body;
    } while ($expr);
    
    do {
        // structure body;
    } while (
        $expr1
        && $expr2
    );
    ```
    
    #### 5-4. switch
    ```
    switch ($expr) {
        case 0:
            echo 'First case, with a break';
            break; // Correct
        case 1:
            echo 'Second case, which falls through'; // Incorrect
        case 2:
        case 3:
        case 4:
            echo 'Third case, return instead of break';
            return;
        default:
            echo 'Default case';
            break;
    }
    ```
    
    #### 5-5. try, catch, finally
    ```
    try {
        // try body
    } catch (FirstThrowableType $e) {
        // catch body
    } catch (OtherThrowableType | AnotherThrowableType $e) {
        // catch body
    } finally {
        // finally body
    }
    ```
<br>

### 6. Operators (연산자)
* Unary (단항)
- [x] Correct
    ```
    $value++;
    --$value;
    $a = !$b;
    $c = +$d;
    $e = -$f;
    ```
- [ ] Incorrect

* Binary (이진)
```
if ($a === $b) {
    $foo = $bar ?? $a ?? $b;
} elseif ($a > $b) {
    $foo = $a + $b * $c;
} elseif ($a <=> $c) {
    $foo += $bar % $a & $b ** $c;
}
```

* Ternary (3항)
```
$variable = $foo ? 'foo' : 'bar';
$variable = $foo ?: 'bar';
```

#### 7. 연산
- [x] Correct
```
a = b + c;
d = a + r;
```
- [ ] Incorrect
```
d = (a = b + c) + r;
```
<br><br>

### 8. Comment (주석)
```
/**
 * @brief 기본설명
 * @author 작성자 - 여러명일 경우 콤마(,)로 구분
 * @param 파라미터(매개변수)의 설명
 * @return 리턴의 자료형 설명
 * @see 참고사항, 추가적으로 알아야 할 사항이 있다면 작성
 * @todo 추가적으로 해야 할 사항 정리
 */
```
```
/*
여러줄로
주석이 가능하죠
*/
```
```
// comment
```
<br><br>

### 9. Dataset (데이터셋)

<br><br>

<hr>

### JavaScript
* https://ui.toast.com/fe-guide/ko_CODING-CONVENTION
* `const`를 `let`보다 위에 선언
* `var` 사용금지

<hr>

### CSS
* 들여쓰기 금지. 단 중괄호`{ }`가 중첩되는 경우 예외
* 공백 최소화
* 빈 줄로 그룹 영역 표시
* HTML 인코딩과 동일하게 선언
* z-index 속성 값을 범위에 맞게 표현
* 크로스 브라우징 위해 제시된 핵(hack) 최소한으로 사용<br>
![Structure](https://mybox.naver.com/share/list/viewer/3472477165626496077?shareKey=e1TCo4K1uJsq_kIroDZ6wc82Yf5-7_2W0MD5JwYA_D6FW1Ov4rbCOYHyCWePU9HMeVjcuHjtrHPmwJcvYDiMtAY=)
<br><br>








----------------------------------
## Reference
https://psr.kkame.net/accepted/psr-1-basic-coding-standard   
https://www.php-fig.org/psr/psr-2/
https://www.lesstif.com/laravelprog/php-psr-24445325.html
https://psr.kkame.net/deprecated/psr-2-coding-style-guide

### MarkDown
https://blog.naver.com/crud0626/222716270890   
https://gist.github.com/ihoneymon/652be052a0727ad59601
https://blog.naver.com/sobrightlf/222535709749

### 참고
https://developer.wordpress.org/coding-standards/wordpress-coding-standards/php/

https://nuli.navercorp.com/data/convention/NHN_Coding_Conventions_for_Markup_Languages.pdf
https://velog.io/@hyundong_kk/%EC%BD%94%EB%93%9C-%EC%BB%A8%EB%B2%A4%EC%85%98
https://myeonguni.tistory.com/1596
https://developer-c.tistory.com/25
https://overcome-the-limits.tistory.com/5?category=923736
