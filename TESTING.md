# Testing

Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

## Manual Testing

| Feature | Expected Result (with evidence) | Result |
|---|---|---|
| Home page loads | Page displays correctly. ![Home](documentation/home.png) | ✅ Pass |
| Register user | User account created successfully. ![Signup](documentation/signup.png) | ✅ Pass |
| Login | User logs in successfully. ![Login](documentation/html-login.png) | ✅ Pass |
| Create booking | Booking form loads and submits successfully. ![Booking Form](documentation/booking-form.png) | ✅ Pass |
| Date selector | Date can be selected on booking form. ![Date Selector](documentation/date-selector.png) | ✅ Pass |
| Notes field | Notes field accepts text input. ![Notes](documentation/notes.png) | ✅ Pass |
| My bookings | User can view their bookings dashboard. ![My Bookings](documentation/my-bookings.png) | ✅ Pass |
| No bookings state | Message shown when user has no bookings. ![No Bookings](documentation/no-bookings.png) | ✅ Pass |
| Edit booking | Booking can be edited successfully. ![Edit](documentation/edit.png) | ✅ Pass |
| Delete booking | Booking can be deleted successfully. ![Delete](documentation/delete.png) | ✅ Pass |
| Delete CSRF protection | Delete uses POST + CSRF confirmation. ![CSRF Delete](documentation/csrf-delete.png) | ✅ Pass |
| Admin panel | Admin page accessible. ![Admin](documentation/admin.png) | ✅ Pass |


## CSS Validation (W3C)

CSS was tested using [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and found no issues.

| Page / Stylesheet | Evidence | Result |
|---|---|---|
| Home CSS | ![CSS Home](documentation/css-home.png) | ✅ Pass |
| Login CSS | ![CSS Login](documentation/css-login.png) | ✅ Pass |
| Signup CSS | ![CSS Signup](documentation/css-signup.png) | ✅ Pass |
| Booking CSS | ![CSS Booking](documentation/css-book.png) | ✅ Pass |
| Edit CSS | ![CSS Edit](documentation/css-edit.png) | ✅ Pass |
| My Bookings CSS | ![CSS My Bookings](documentation/css-mybookings.png) | ✅ Pass |
| Delete CSS | ![CSS Delete](documentation/css-delete.png) | ✅ Pass |

## Python (PEP8) Validation

| File | Location | Evidence | Result |
|---|---|---|---|
| `admin.py` | bookings/admin.py | ![admin.py](documentation/admin.png) | ✅ Pass |
| `apps.py` | bookings/apps.py | ![apps.py](documentation/apps.png) | ✅ Pass |
| `models.py` | bookings/models.py | ![models.py](documentation/models.png) | ✅ Pass |
| `views.py` | bookings/views.py | ![views.py](documentation/views.png) | ✅ Pass |
| `forms.py` | bookings/forms.py | ![forms.py](documentation/forms.png) | ✅ Pass |
| `urls.py` | bookings/urls.py | ![urls.py](documentation/views.png) | ✅ Pass |
| `settings.py` | the_polite_pup/settings.py | ![settings.py](documentation/settings.png) | ✅ Pass |


## Lighthouse Reports

I tested my deployed project using the Lighthouse Audit tool to check for any issues. The site came back with no issues.

| Page | Evidence |
|---|---|
| Home | ![Lighthouse Home](documentation/lighthouse-home.png) |
| Register | ![Lighthouse Register](documentation/lighthouse-register.png) |
| Booking | ![Lighthouse Booking](documentation/lighthouse-booking.png) |
| My Bookings | ![Lighthouse MyBookings](documentation/lighthouse-mybookings.png) |
| Delete | ![Lighthouse Delete](documentation/lighthouse-delete.png) |


## Browser Compatibility

| Browser | Evidence | Result |
|---|---|---|
| Chrome | ![Chrome](documentation/home.png) | ✅ Pass |
| Edge | ![Edge](documentation/edge.png) | ✅ Pass |
| Firefox | ![Firefox](documentation/firefox.png) | ✅ Pass |
| Safari | *(tested on device)* | ✅ Pass |

## Responsiveness Testing

| Device | Evidence | Result |
|---|---|---|
| Mobile | ![Mobile](documentation/mobile.png) | ✅ Pass |
| Tablet | ![Tablet](documentation/tablet.png) | ✅ Pass |
| Desktop | ![Desktop](documentation/home.png) | ✅ Pass |

