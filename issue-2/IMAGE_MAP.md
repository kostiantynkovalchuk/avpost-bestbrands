# AV Post №2 — image map (placeholder in index.html → source on Google Drive «Корпоративная газета»)

Put every file into `images/` under the exact target name, then run `inline_images.py`.

## Маркетинг (folder «Газета от маркетинга»)
| target | source |
|---|---|
| greenday_apple.jpg | image embedded in `GREENDAY APPLE — яблучний смак, який варто спробувати.docx` (extract; or product shot from marketing) |
| setter_dry.jpg | image embedded in `Setter Royal Dry_Orange.docx` (Dry bottle) |
| setter_orange.jpg | image embedded in `Setter Royal Dry_Orange.docx` (Orange bottle) — if docx contains one combined image, use it for both and set the second `<figure>` to `display:none` ⚠ |
| bridgerton_1.png | `Бріджертони 1.png` |
| bridgerton_2.png | `Бріджертони 2.png` |
| hosteviia_1.png | `Гостевія 1.png` |
| hosteviia_2.png | `Гостевія 2.png` |
| influence.jpg | `Інфлюенс маркетинг Frizzante.jpg` |
| el_terrole.jpg | `El Terrole.jpg` |
| adjari_coffee.png | `Adjari Coffee.png` |

## Продажи (folder «Газета от Саши»)
| target | source |
|---|---|
| naduiev.jpg | portrait embedded in `Інтерв'ю Надуєв.doc` ⚠ verify it exists |
| korol.jpg | portrait embedded in `Інтерв'ю Король.doc` ⚠ |
| pustovyt.jpg | portrait embedded in `Інтерв'ю Пустовит.doc` ⚠ |
| lozova.jpg | portrait embedded in `Інтерв'ю Лозова.doc` ⚠ |
| bezzubenko.jpg | `Герої полів/Беззубенко.jpg` |
| riabtsun.jpg | `Герої полів/Рябцун.jpg` |
| fitiak.jpg | `Герої полів/Фітяк.jpg` |
| manko.jpg | `Герої полів/Манько.jpg` |
| chupa.jpg | `Герої полів/Чупа.jpg` |
| dilovyi.jpg | `Герої полів/Діловий.jpg` |
| training_dp_1.png | `Кайдзен/` group photo, Vinnytsia (widest one) |
| training_dp_2.png | `Кайдзен/` second Vinnytsia photo |
| training_sv.jpg | `Кайдзен/` Khmelnytskyi supervisors photo |
| motivation_volyn.jpg | `Мотивация Аджари/Волинь1.jpg` |
| motivation_20years.jpg | `Мотивация Аджари/ДР филиала 20 лет.jpg` ⚠ caption: file name suggests a branch anniversary, not the Adjari event — confirm with Саша |
| motivation_3.jpg | `Мотивация Аджари/photo_2026-04-29.jpg` |

## HR (folders «Зоопарк», «Улюбленці»)
| target | source |
|---|---|
| chuyka_1.jpg | image embedded in `Чуйка.docx` (device/car photo) |
| zoo_1.png … zoo_7.png | `Зоопарк/1.png … 7.png` (zoo_1 = hero full-bleed, pick the widest) |
| pet_reshetilova.jpg | `Наталя Решетілова — Оливка` |
| pet_melikhov.jpg | `Олег Меліхов — Зевс` |
| pet_korinnoi.jpg | `Олександр Корінной — Амадей та Апельсин` |
| pet_burkovska.jpg | `Ірина Бурковська — Швіцвард` |
| pet_burian.jpg | `Оля Бур'ян — Марсель` |
| pet_herasymova.jpg | `Катерина Герасимова — Кіндер` |
| pet_lohai.jpg | `Ольга Логай — Степан` |
| pet_andrieieva.jpg | `Саша Андрєєва — Буфер` |
| pet_shyhymaha.jpg | `Оксана Шигимага — Ванілька та Булочка` |
| pet_trofymchuk.jpg | `Юлія Трофимчук — Ігор Володимирович` |
| pet_voloshchuk.jpg | `Валентин Волощук — Фанта Хердерсхил` |
| pet_mykhailova.jpg | `Лілія Михайлова — Мійя` |
| pet_horaichuk.jpg | `Катерина Горайчук — Міка` |
| pet_seimskyi.jpg | `Олександр Сеймський — Дейзі Джаз` |
| pet_volodko.jpg | `Юля Володько — Лучик` |

Extension mismatch is fine — the inline script reads whatever is on disk with the same basename.
