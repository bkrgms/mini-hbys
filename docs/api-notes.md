# Public API Kullanımı

## randomuser.me
Doktor isimleri için kullanıldı (Faker'a ek olarak, gerçek bir dış API'den 
veri çekme pratiği yapmak amacıyla).

Endpoint: https://randomuser.me/api/?results=5&nat=tr
Auth gerekmiyor, ücretsiz.

`scripts/fetch_reference_data.py` dosyasında kullanımı var.