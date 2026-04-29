FROM eclipse-temurin:21-jdk
WORKDIR /app
COPY Main.java /app/Main.java
RUN javac Main.java
RUN useradd --create-home --uid 10002 appuser && chown -R appuser:appuser /app
USER appuser
EXPOSE 8082
CMD ["java", "Main"]
