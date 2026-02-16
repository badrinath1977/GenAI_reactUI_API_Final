USE GenAI;
GO

PRINT '==============================';
PRINT '1️⃣  VERIFY TABLE RECORD COUNTS';
PRINT '==============================';

SELECT 
    (SELECT COUNT(*) FROM dbo.FileMetadata) AS TotalFiles,
    (SELECT COUNT(*) FROM dbo.UserPromptLog) AS TotalPrompts,
    (SELECT COUNT(*) FROM dbo.ErrorLog) AS TotalErrors;
GO


PRINT '==============================';
PRINT '2️⃣  FILE METADATA - LATEST RECORDS';
PRINT '==============================';

SELECT TOP 20 *
FROM dbo.FileMetadata
ORDER BY Id DESC;
GO


PRINT '==============================';
PRINT '3️⃣  FILE TYPE DISTRIBUTION';
PRINT '==============================';

SELECT FileExtension, COUNT(*) AS TotalFiles
FROM dbo.FileMetadata
GROUP BY FileExtension
ORDER BY TotalFiles DESC;
GO


PRINT '==============================';
PRINT '4️⃣  DUPLICATE FINGERPRINT CHECK';
PRINT '==============================';

SELECT FingerPrint, COUNT(*) AS DuplicateCount
FROM dbo.FileMetadata
GROUP BY FingerPrint
HAVING COUNT(*) > 1;
GO


PRINT '==============================';
PRINT '5️⃣  USER PROMPT LOG - LATEST';
PRINT '==============================';

SELECT TOP 20 *
FROM dbo.UserPromptLog
ORDER BY CreatedDate DESC;
GO


PRINT '==============================';
PRINT '6️⃣  MODEL USAGE SUMMARY';
PRINT '==============================';

SELECT Provider, ModelUsed, COUNT(*) AS UsageCount
FROM dbo.UserPromptLog
GROUP BY Provider, ModelUsed
ORDER BY UsageCount DESC;
GO


PRINT '==============================';
PRINT '7️⃣  ERROR LOG - LATEST';
PRINT '==============================';

SELECT TOP 20 *
FROM dbo.ErrorLog
ORDER BY CreatedDate DESC;
GO


PRINT '==============================';
PRINT '8️⃣  ERROR TYPE SUMMARY';
PRINT '==============================';

SELECT ErrorType, COUNT(*) AS TotalErrors
FROM dbo.ErrorLog
GROUP BY ErrorType
ORDER BY TotalErrors DESC;
GO


PRINT '==============================';
PRINT '9️⃣  VERIFY STORED PROCEDURES';
PRINT '==============================';

SELECT name AS StoredProcedureName
FROM sys.procedures
WHERE name LIKE 'sp_%'
ORDER BY name;
GO


PRINT '==============================';
PRINT '✅ VERIFICATION COMPLETED';
PRINT '==============================';
