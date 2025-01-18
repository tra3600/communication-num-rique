SELECT DISTINCT auteur
FROM corpus;

SELECT 
    c.symbole, 
    SUM(o.nombreOccurrences) / (SELECT SUM(co.nombreCaracteres) 
                                FROM corpus co 
                                WHERE co.langue = 'Français') AS frequence
FROM 
    occurrences o
JOIN 
    caractere c ON o.idCar = c.idCar
JOIN 
    corpus co ON o.idLivre = co.idLivre
WHERE 
    co.langue = 'Français'
GROUP BY 
    c.symbole;