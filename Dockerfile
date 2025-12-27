# 1️⃣ Base image
FROM python:3.11-slim

# 2️⃣ Set working directory
WORKDIR /app

# 3️⃣ Copy dependency file first (layer caching)
COPY requirements.txt .

# 4️⃣ Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Copy application code
COPY . .

# 6️⃣ Expose Flask port
EXPOSE 5000

# 7️⃣ Run app via wsgi
CMD ["python", "wsgi.py"]
