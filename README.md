![GitHub language count](https://img.shields.io/github/languages/count/bluecara/lab-src)
![GitHub top language](https://img.shields.io/github/languages/top/bluecara/lab-src)
![GitHub repo file or directory count](https://img.shields.io/github/directory-file-count/bluecara/lab-src)
![GitHub last commit](https://img.shields.io/github/last-commit/bluecara/lab-src)
![GitHub Repo stars](https://img.shields.io/github/stars/bluecara/lab-src)

# Coding Conventions

### 1. Overview
* 협업을 중점으로 (쉽게 읽히는) 좋은 코드로 작성하기
* base on PSR : https://www.php-fig.org/psr/psr-2/
* https://developer.wordpress.org/coding-standards/wordpress-coding-standards/php/
<br><br>

### 2. Basic
* Common
    + 괄호, 쉼표, 공백 및 중괄호`{}`의 배치에 유의
    + 숫자로 시작 No
    + 약어 사용 No
    + 괄호 `()` 사이에 공백 No
    + 인수 목록 각 쉼표 앞에 공백 No, 쉼표 뒤에 공백 하나 Yes
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
    |model|*.model.php|
    |Template|*.tpl|
* Quotation Mark
    + HTML / Query / reqular expressions : 쌍타옴표 `"`
    + PHP code / Javascript : 홀따옴표 `'`
* Indenting
    + 4 space
    + tab 사용 No
* Naming
    + Class : `PascalCase`
        - ex) ClassName
    + Variable / Parameter : `camelCase`
        - ex) helloWorld
    + Method / Function : 동사/전치사 + `camelCase`
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
* hyphen `-` , under_score `_` 사용 No
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
    > + 이름 다음에 공백 No
    > + 연산자 `&` 를 사용하면 뒤에 공백 No
    ```
    public funciton fooBarBaz($arg1, &$arg2, $arg3 = [], &...$arg4) {
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
* 제어 구조 키워드 다음에 하나의 공백 Yes
* 닫는 괄호 `)` 와 여는 중괄호 `{` 사이에 하나의 공백 Yes
* 본문은 한 번 **들여쓰기** Yes
* 닫는 중괄호 `}` 는 몸체 뒤의 다음 줄 Yes
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
    ```
    try {
        echo inverse(5) . "\n";
        echo inverse(0) . "\n";
    } catch (Exception $e) {
        echo 'Caught exception: ' . $e->getMessage() . ' (Code : ' . $e->getCode() . ")\n";
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
    ```
    $value(++(++));
    $value++ ++;
    ```

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

### 9. Database
* Common
    + 예약어 사용 No
        - ex) table, all, add, check, drop, if, set, insert, update 등
    + 약어 사용 No
        - ex) _TB, _CD, _NO, _TM 등
    + 직관적인 `기술형`으로 작성
        - 되도록 쉬운 단어 선택
        - 의미없는 숫자 뒤에 붙이지 않음
    + `단수(singular)형`을 사용
        - ex) member : Yes / members : No
    + 공백을 포함시키지 않음
    + `설명 반드시 작성`
    + 길이는 최대 30바이트까지만 사용
    + 문자로 시작하고, 밑줄로 끝나면 안 됨

* Table
    + `PascalCase` 로 작성
        - ex) User , UserLog
    + 테이블의 컬럼과 동일한 이름 사용 No
    + 접두사 사용 금지
    + Engine : InnoDB
    + Charset : utf8 / utf8mb4
    + Collation : utf8mb4_unicode_ci

* Column
    + `snake_case` 로 작성
    + 영문 소문자와 under_score `_` 로 조합
        - ex) auth_user
    + 테이블과 이름이 같은 컬럼 생성 금지
    + 데이터 유형을 이름으로 작성하지 않음
        - ex) abc_timestamp , abc_text
    + 한 단어는 8자리를 넘기지 않음
    + 필수값 조건 꼭 넣기
    + 가능하면 기본키의 이름을 `id` 로 사용 금지
    + `소문자`로 작성
        - [X] Correct
        ```
        create_date, user_code
        ```
        - [ ] Incorrect
        ```
        create_dt, user_cd
        ```
    + 컬럼 타입에 맞는 `접두사`, `접미사` 통일해서 사용
        - 일련번호 : seq 로 통일
        - 숫자형 : <Column Name> + _count
        - 날짜형 : <Column Name> + _date
        - Boolean형 : is_ + <Column Name>

* Data type
    + Text
        - char(M) : 고정 길이를 가지는 문자열을 저장한다. (M : 0~255)
        - varchar(M) : 가변 길이를 가지는 문자열을 저장하며, 후행 공백을 제거하지 않는다. (M : 0~65,535)
M이 0~255 이면 문자길이+1byte, ~65,535 이면 문자길이+2byte
        - tinyblob / tinytext : 1~255 개의 가변 길이를 가지는 문자열을 저장한다. (문자길이+1byte)
        - blob / text : 1~65,535 개의 가변 길이를 가지는 문자열을 저장한다. (문자길이+2byte)
BLOB 는 바이너리 데이터, TEXT 는 문자 데이터 저장에 유리하다.
        - mediumblob / mediumtext : 1~16,777,215 개의 가변 길이를 가지는 문자열을 저장한다. (문자길이+3byte)
        - longblob / longtext : 1~429,496,729 개의 가변 길이를 가지는 문자열을 저장한다. (문자길이+4byte)
        - enum : 문자 형태인 value 를 숫자로 저장하여 최대 65,535 개의 문자열 중 한가지를 반환
255 이하 value 는 1바이트, 65,535 이하 value 는 2바이트 (반드시 하나의 값만 저장)
        - set : 비트 연산 열거형, ENUM 형과 동일하게 문자열 값을 정수값으로 매핑하여 저장한다. (다중 선택 가능)
    + Date
        - date : 날짜를 표현하는 타입 (3바이트)
            ```
            1000-01-01 ~ 9999-12-31
            ```
        - `datetime` : 날짜와 시간을 같이 나타내는 타입 (8바이트)
            ```
            1000-01-01 00:00:00 ~ 9999-12-31 23:59:59
            ```
        - timestamp : INSERT, UPDATE 연산에 유리하다. (4바이트)
            ```
            1970-01-01 00:00:00 ~ 2037-01-19 03:14:07
            ```
        - time : 시간을 표현하는 타입 (3바이트)
            ```
            -838:59:59 ~ 838:59:59
            ```
        - year : 연도를 나타낸다. (1바이트)
            ```
            1901 ~ 2155, 70 ~ 69 (1970~2069)
            ```
            https://dev.mysql.com/doc/refman/8.0/en/two-digit-years.html
    + Number
        - bit : 비트값 타입. 즉, 0과 1로 구성되는 binary 값을 저장한다. (M : 1~64, 생략 시 기본값은 1 로 설정)
        - bool : 0은 false, 0이 아닌 값은 true 로 간주하는 논리형 데이터. ENUM(Y,N) 또는 TINYINT(1) 로 대체하여 사용하는 것을 권장
        - tinyint(M) : 부호 있는 수는 -128 ~ 127 / 부호 없는 수는 0 ~ 225 까지 표현 (1바이트)
        - smallint(M) : 부호 있는 수는 -32768 ~ 32767 / 부호 없는 수는 0 ~ 65535 까지 표현 (2바이트)
        - mediumint(M) : 부호 있는 수는 -8388608 ~ 8388607 / 부호 없는 수는 0 ~ 16777215 까지 표현 (3바이트)
        - int(M) / integer(M) : 부호 있는 수는 -2147483648 ~ 2147483647 / 부호 없는 수는 0 ~ 4294967295 까지 표현 (4바이트)
        - bigint(M) : 부호 있는 수는 -92233720036854775808 ~ 92233720036854775807 / 부호 없는 수는 0~18446744073709551615 (8바이트)
        - DECIMAL(M,D) : M자리 정수(정밀도)와 D자리 소수점(스케일)으로 표현. 최대 65자리까지 표현할 수 있다. (회계/정산)
        - float(M,D) : 정밀도가 작은 부동소수점을 표현. UNSIGNED 인 경우 음수 값을 허용하지 않는다.
            ```
            -3.402823466E+38 ~ 3.402823466E+38
            ```
        - double(M,D) : 보통 크기의 부동소수점을 표현. UNSIGNED 인 경우 음수 값을 허용하지 않는다.
            ```
            -1.7976931348623157E+308 ~ 1.7976931348623157E+308
            ```
        https://dev.mysql.com/doc/refman/8.0/en/problems-with-float.html

* Primary Key
    + 영문 대문자로 작성
        - ex) <Table Name> + _PK

* Foreign Key
    + 영문 대문자로 작성
    + 일련번호 : 1 ~ 9 (선택)
        - ex) <Table Name> + _FK + {일련번호}

* Index
    + 영문 대문자로 작성
    + 의미있는 컬럼 이름 추가 가능
    + 일련번호 : 01 ~ 99 (선택)
        - ex) <Table Name> + <Column Name> + _IDX + {일련번호}

<br><br>

<hr>

### JavaScript
* https://ui.toast.com/fe-guide/ko_CODING-CONVENTION
* `const`를 `let`보다 위에 선언
* `var` 사용금지

<br><br>

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
