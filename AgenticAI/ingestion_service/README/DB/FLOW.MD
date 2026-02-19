Excellent 👍 Badri — now we’ll define the **clear execution flow of Tables + Stored Procedures** in your finalized `EnterpriseGenAI` database.

I’ll explain this in a **system-level architectural way**, so you can present this to Architect/Manager.

---

# 🏗 OVERALL SYSTEM FLOW (DB Perspective)

We have 3 major flows:

1️⃣ File Upload Flow
2️⃣ File Replacement Flow
3️⃣ RAG Query Flow
4️⃣ Error Handling Flow
5️⃣ Usage & Prompt Logging Flow

---

# 🟢 1️⃣ FILE UPLOAD FLOW (NEW FILE)

### 🎯 Scenario:

User uploads a new document.

---

## 🔁 Flow Diagram (DB Level)

```
API Layer
   ↓
Generate SHA256 ContentHash
   ↓
sp_GetActiveFileByHash
   ↓
IF EXISTS → STOP (Duplicate Content)
   ↓
sp_GetActiveFileByName
   ↓
IF NOT EXISTS → Insert New File
   ↓
sp_InsertFileMetadata
   ↓
Return NewFileId
```

---

## 🧠 Stored Procedures Used

### 1️⃣ `sp_GetActiveFileByHash`

Purpose:

* Prevent duplicate content
* Avoid unnecessary vector processing

```sql
EXEC ApplicationChatbot.sp_GetActiveFileByHash @ContentHash
```

---

### 2️⃣ `sp_GetActiveFileByName`

Purpose:

* Check if same logical document exists

```sql
EXEC ApplicationChatbot.sp_GetActiveFileByName @FileName
```

---

### 3️⃣ `sp_InsertFileMetadata`

Purpose:

* Insert new document metadata
* Returns NewFileId (used for vector tagging)

```sql
EXEC ApplicationChatbot.sp_InsertFileMetadata ...
```

---

# 🟡 2️⃣ FILE REPLACEMENT FLOW

### 🎯 Scenario:

Same filename exists but content hash is different.

---

## 🔁 Flow Diagram

```
Upload Request
   ↓
Generate SHA256
   ↓
sp_GetActiveFileByHash → NOT FOUND
   ↓
sp_GetActiveFileByName → FOUND
   ↓
User Confirms Replace
   ↓
sp_MarkFileInactive (Old File)
   ↓
Vector Delete by FileId
   ↓
sp_InsertFileMetadata (New Version)
   ↓
NewFileId Returned
```

---

## 🧠 Stored Procedures Used

### 1️⃣ `sp_MarkFileInactive`

Purpose:

* Soft delete old version
* Maintain audit trail

```sql
EXEC ApplicationChatbot.sp_MarkFileInactive
    @FileId = 10,
    @Reason = 'Replaced by newer version'
```

This updates:

```sql
IsActive = 0
InactivatedReason = 'Replaced by newer version'
```

---

# 🟣 3️⃣ RAG QUERY FLOW

### 🎯 Scenario:

User asks question.

---

## 🔁 Flow Diagram

```
User Question
   ↓
Vector DB Retrieval (Filter: IsActive=1)
   ↓
LLM Call
   ↓
sp_InsertPromptLog
   ↓
Store question/response/tokens
```

---

## 🧠 Stored Procedures Used

### `sp_InsertPromptLog`

```sql
EXEC ApplicationChatbot.sp_InsertPromptLog
    @UserName,
    @Provider,
    @Model,
    @Question,
    @Response,
    @TokensUsed,
    @Department
```

Purpose:

* Audit AI usage
* Track token consumption
* Monitor per user & per model usage

---

# 🔴 4️⃣ ERROR FLOW

### 🎯 Scenario:

Any exception in upload/query.

---

## 🔁 Flow Diagram

```
Exception Occurs
   ↓
Middleware catches
   ↓
sp_InsertErrorLog
   ↓
Flat file logging
   ↓
Return TraceId to user
```

---

## 🧠 Stored Procedure Used

### `sp_InsertErrorLog`

```sql
EXEC ApplicationChatbot.sp_InsertErrorLog
    @TraceId,
    @UserId,
    @ErrorType,
    @ErrorMessage,
    @StackTrace
```

Purpose:

* Centralized error tracking
* Correlation using TraceId
* Enterprise audit compliance

---

# 🔵 5️⃣ USAGE MONITORING FLOW

For dashboard / reporting:

### System Usage

```sql
EXEC ApplicationChatbot.sp_GetSystemUsage
```

Returns:

* TotalRequests
* TotalTokens
* Per Model
* Per Provider

---

### User Usage

```sql
EXEC ApplicationChatbot.sp_GetUserUsage @UserName
```

Purpose:

* Billing
* Rate limiting
* Governance

---

# 🏛 TABLE ROLE SUMMARY

| Table                   | Purpose                       |
| ----------------------- | ----------------------------- |
| FileMetadata            | Document lifecycle management |
| application_logs        | Request/Response logging      |
| ErrorLog                | Exception tracking            |
| PromptLog               | AI usage tracking             |
| EmbeddingProviderConfig | Embedding provider config     |
| LLMProviderConfig       | LLM config                    |
| SensitiveDataRules      | Data masking rules            |
| SensitiveAudit          | Sensitive detection audit     |

---

# 🔥 FULL END-TO-END ENTERPRISE FLOW

```
Upload File
   ↓
ContentHash Generated
   ↓
Check Duplicate (Hash)
   ↓
Check Logical Document (Name)
   ↓
Replace or Insert
   ↓
Vector Tagging by FileId
   ↓
User Query
   ↓
Retrieve Only Active File Vectors
   ↓
LLM
   ↓
PromptLog Stored
   ↓
Errors Stored (If Any)
```

---

# 🎯 WHY THIS DB DESIGN IS STRONG

✔ Deterministic duplicate detection
✔ Logical document grouping
✔ Soft delete audit trail
✔ TraceId based monitoring
✔ No physical data loss
✔ Enterprise governance ready
✔ Supports vector lifecycle
✔ Supports AI billing monitoring

---

# 🏆 ARCHITECT SUMMARY YOU CAN PRESENT

We implemented a deterministic content-hash-based document lifecycle strategy. The database ensures strict version control, soft deletion for audit compliance, and selective vector lifecycle management. RAG retrieval only operates on active documents, preventing hallucination from outdated content while maintaining full historical traceability.

---

# 🚀 NEXT STEP

Now that DB flow is finalized:

Do you want me to:

1️⃣ Map this DB flow to Python repository layer with full transaction handling?
2️⃣ Create sequence diagram for presentation?
3️⃣ Create API contract document?
4️⃣ Move to vector lifecycle finalization?

Tell me the next layer to finalize.
