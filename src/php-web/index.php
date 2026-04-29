<?php
header('Content-Type: text/plain; charset=utf-8');
echo "Hallo Welt aus PHP\n";
$apiUrl = getenv('PYTHON_API_URL') ?: 'http://python-api:8000';
echo "Python-API: " . $apiUrl . "\n";
