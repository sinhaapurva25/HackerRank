SELECT CASE 
		WHEN A+B > C THEN CASE
			WHEN A=B AND B=C THEN "Equilateral"
			WHEN A=B OR B=C OR C=A THEN "Isosceles"
			WHEN A!=B AND B!=C AND C!=A THEN "Scalene"
        END
		ELSE "Not A Triangle"
    END
FROM TRIANGLES;