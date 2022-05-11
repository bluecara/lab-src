# Coding Conventions

### 1. Overview
* base on PSR : https://www.php-fig.org/psr/psr-2/
<br><br>

### 2. Basic
* Default
    + 괄호, 공백 및 중괄호의 배치, 공백에 유의
* File
    + `<?php` / `<?=` 태그만 사용
    + PHP code만 존재 → `?>` 태그 생략
    + Type : Unix
    + Character Encoding : BOM이 없는 UTF-8
* Extension
    + html로 파일 저장
    + php로 저장 : common/include 형태 등
        - *.ajax.php / *.inc.php
* Quotation Mark
    + HTML 태그 : `"`
    + PHP code / 자바스크립트 : `'`
* Indenting
    + 4 space
    + tab 사용 안함
<br><br>

### Class (클래스)
* 클래스명은 `StudlyCaps` 규칙 사용
* `_` 은 사용 안함
* 여는 중괄호 / 닫는 중괄호는 반드시 다음줄에 명시
    ```
    class ClassName extends ParentClass
    {
        // constants, properties, method
    }
    ```

    #### Constants
    > + 모두 대문자와 밑줄`_` 만으로 선언
    ```
    const VERSION = '1.0';
    const DATE_APPROVED = '2012-06-01';
    ```
    ```
    public $foo = null;
    public static int $bar = 0;
    ```

    #### Methods & Functions
    > + `camelCase`로 작성
    > + 이름 다음에 공백 X
    > + 여는 중괄호 / 닫는 중괄호는 반드시 다음줄에 명시
    > + 괄호, 쉼표, 공백 및 중괄호의 배치에 유의
    > + 연산자 `&`를 사용하면 뒤에 공백 X
    ```
    public funciton fooBarBaz($arg1, &$arg2, $arg3 = [], &...$arg4)
    {
        // method body
    }
    ```
    > + 인수 목록이 여러줄로 표시할 경우, 각 줄에 한 번 들여쓰기 추가
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
    
    > + 호출시 여는 괄호 사이에 공백 X
    > + 여는 괄호 뒤에 공백 X
    > + 닫는 괄호 앞에 공백 X
    > + 인수 목록 각 쉼표 앞에 공백 X, 쉼표 뒤에 공백 하나 O
    ```
    bar();
    bar(...['foo','bar']);
    $foo->bar($arg1);
    Foo::bar($arg2, $arg3);
    ```
    
    #### Anonymous - 익명
    ```
    $instance = new class {};
    ```

### Control (제어)
* 제어 구조 키워드 다음에 하나의 공백 O
* 여는 괄호 뒤에 공백 X
* 닫는 괄호 앞에 공백 X
* 닫는 괄호와 여는 중괄호 사이에 하나의 공백 O
* 본문은 한 번 **들여쓰기** O
* 닫는 중괄호는 몸체 뒤의 다음 줄 O
    #### if, elseif, else
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
    
    #### for, foreach
    ```
    for ($i = 0; $i < 10; $i++) {
        // for body
    }
    foreach ($iterable as $key => $value) {
        // foreach body
    }
    ```
    
    #### while, do while
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
    
    #### switch
    ```
    switch ($expr) {
        case 0:
            echo 'First case, with a break';
            break;
        case 1:
            echo 'Second case, which falls through';
            break;
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
    
    #### try, catch, finally
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

### Operators (연산자)
    #### Unary (단항)
    ```
    $value++;
    --$value;
    $a = !$b;
    $c = +$d;
    $e = -$f;
    ```
    
    #### Binary (이진)
    ```
    if ($a === $b) {
        $foo = $bar ?? $a ?? $b;
    } elseif ($a > $b) {
        $foo = $a + $b * $c;
    } elseif ($a <=> $c) {
        $foo += $bar % $a & $b ** $c;
    }
    ```
    
    #### Ternary (3항)
    ```
    $variable = $foo ? 'foo' : 'bar';
    $variable = $foo ?: 'bar';
    ```

### Dataset


----------------------------------
## Reference
https://psr.kkame.net/accepted/psr-1-basic-coding-standard   
https://www.php-fig.org/psr/psr-2/

### MarkDown
https://blog.naver.com/crud0626/222716270890   
https://gist.github.com/ihoneymon/652be052a0727ad59601
https://blog.naver.com/sobrightlf/222535709749

### 참고
https://psr.kkame.net/deprecated/psr-2-coding-style-guide
https://www.php-fig.org/psr/psr-2/
https://developer.wordpress.org/coding-standards/wordpress-coding-standards/php/

https://nuli.navercorp.com/data/convention/NHN_Coding_Conventions_for_Markup_Languages.pdf
https://ui.toast.com/fe-guide/ko_CODING-CONVENTION
https://velog.io/@hyundong_kk/%EC%BD%94%EB%93%9C-%EC%BB%A8%EB%B2%A4%EC%85%98
https://myeonguni.tistory.com/1596
https://developer-c.tistory.com/25
https://overcome-the-limits.tistory.com/5?category=923736
