-- Напишите SQL-запрос, который возвращает ТОП-5 самых продаваемых курсов по месяцам.
WITH monthly_sales AS (
    SELECT
        course_id,
        DATE_TRUNC('month', order_date) AS month,
        COUNT(*) AS sales_count
    FROM orders
    GROUP BY course_id, month
)
SELECT
    c.course_name,
    ms.month,
    ms.sales_count
FROM monthly_sales ms
JOIN courses c ON ms.course_id = c.course_id
ORDER BY ms.month, ms.sales_count DESC
LIMIT 5;

-- Напишите SQL-запрос, который возвращает ТОП-3 самых популярных пакетов по предметам.
WITH subject_sales AS (
    SELECT
        subject_id,
        course_id,
        COUNT(*) AS sales_count
    FROM orders
    GROUP BY subject_id, course_id
)
SELECT
    s.subjects,
    c.course_name,
    ss.sales_count
FROM subject_sales ss
JOIN subjects s ON ss.subject_id = s.subject_id
JOIN courses c ON ss.course_id = c.course_id
ORDER BY ss.sales_count DESC
LIMIT 3;