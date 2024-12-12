# 📚 검색시사용자 공간 (Chaeksarang Gonggan) | **Book Lover's Haven**

![Logo](main_app/static/images/book.png)

---

## **Table of Contents**

---

## 🖋️ **Description**

Welcome to **Book Lover's Haven** — a creative sanctuary for authors and storytellers! This platform invites writers to bring their imaginations to life with powerful tools to **Create**, **Read**, **Update**, and **Delete** their stories. Whether your passion lies in crafting epic sagas, heartfelt romances, or spine-chilling thrillers, this site caters to all genres.

With an intuitive **authentication system**, authors can create an account to unlock personalized features, such as:

- Writing and managing unlimited stories.
- Tagging stories for effortless organization.
- A user-friendly interface for building a literary universe.

---

## 📊 **Future Features**

### 📸 **Personalized Image Uploads**

- Upload your own PNG images.
- Manage uploaded images privately.
- Delete images when needed.

### 🔗 **Preset Image Gallery**

- Access a curated library of images.
- Enhance stories with visual elements without uploading your own files.

### 🎨 **Enhanced Layouts**

- Leveraging CSS **Flexbox** and **Grid** for modern and responsive designs.
- Future refinements planned for an even more dynamic interface.

---

## 🚀 **Getting Started**

- **Deployed App:** [Your App Link Here]
- **Planning Materials:** [Planning Docs Link]
- **Backend Repository:** [GitHub Link]

---

## 📖 **Attributions**

Include attributions for external libraries, frameworks, or assets used in this project.

---

## 🛠️ **Technologies Used**

- **Backend:** Python, Django
- **Frontend:** HTML, CSS

---

## 🔍 **Models**

### 🔑 **User Model**

| Field    | Type        | Options |
| -------- | ----------- | ------- |
| id       | Primary Key |         |
| username | String      |         |
| password | String      |         |

### 🖊️ **Story Model**

| Field       | Type        | Options           |
| ----------- | ----------- | ----------------- |
| id          | Primary Key |                   |
| name        | String      | max_length=100    |
| description | Text        | max_length=150    |
| story       | Text        |                   |
| photo       | Text        |                   |
| user        | Foreign Key | on_delete=CASCADE |

**Relationship:** Many-to-One with User

### 🔖 **Tag Model**

| Field | Type        | Options                                     |
| ----- | ----------- | ------------------------------------------- |
| id    | Primary Key |                                             |
| name  | String      | max_length=25, choices=TAGS, default=[0][0] |

**Relationship:** Many-to-One with Story

---

## 🌐 **Site Mapping**

| Path                        | View                          | Name           |
| --------------------------- | ----------------------------- | -------------- |
| `/`                         | `views.Home.as_view()`        | `home`         |
| `/about/`                   | `views.about`                 | `about`        |
| `/stories/`                 | `views.story_index`           | `story-index`  |
| `/stories/<int:story_id>`   | `views.story_details`         | `story-detail` |
| `/stories/create/`          | `views.StoryCreate.as_view()` | `story-create` |
| `/stories/<int:pk>/update/` | `views.StoryUpdate.as_view()` | `story-update` |
| `/stories/<int:pk>/delete/` | `views.StoryDelete.as_view()` | `story-delete` |
| `/accounts/signup/`         | `views.signup`                | `signup`       |

---

## 📊 **Next Steps**

- Add support for personalized image uploads.
- Expand the preset image gallery.
- Refine CSS layouts for better usability and performance.

---

## 📚 **Credits**

- [Add credits or contributors here]
