# Thinking Walkthrough — WBS to Schedule

1. รับ Work Package จาก L07 แล้วแตกเป็น activities ที่ estimate/sequence/assign ได้
2. ระบุ dependency logic ก่อนใส่ calendar date
3. ประเมิน duration พร้อม basis, resource และ uncertainty
4. คำนวณ critical path/float และตรวจ external constraints
5. วาง milestones จาก exit evidence ไม่ใช่วันที่ presentation
6. เมื่อ delay เกิด ให้ตรวจ network และ options ก่อนประกาศผลต่อ go-live

Hotel contrast: release date ยังต้องมี dependency/quality gates แม้ทีมส่งมอบเป็นรอบสั้น
