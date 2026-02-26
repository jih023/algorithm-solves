-- 코드를 작성해주세요
SELECT D.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME
FROM DEVELOPERS D
WHERE EXISTS ( SELECT 1
               FROM (SELECT D.SKILL_CODE & S.CODE AS RESULT
                      FROM SKILLCODES S
                      WHERE S.CATEGORY = 'Front End') A
               WHERE A.RESULT <> 0 )
ORDER BY D.ID