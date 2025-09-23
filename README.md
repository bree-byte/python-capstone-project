# Safari Beats - Event Management App

Welcome to 'Safari Beats', a vibrant event management platform celebrating Kenyan cultural heritage through music events. This app allows hosts to add event details and fans to browse and filter events, featuring a colorful design inspired by African rhythms.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Description
Safari Beats connects artists and fans by providing a platform to create, manage, and discover music events with a Kenyan cultural twist. The app includes a Flask backend integrated with Supabase for robust event data storage and a frontend, built with Meku.dev, for an engaging user experience. Dates are now handled correctly with ISO format support.

d<img width="764" height="436" alt="flowchart-image" src="https://github.com/user-attachments/assets/5df17e89-37b3-487d-b971-5f649e5fabe3" />
## Features
- **Host Events**: Add events with details like title, host, tribe, event venue, start date, end date, and ticket link.
- **Browse Events**: View all events with advanced filters by title, host, event venue, or date range.
- **Homepage**: A welcoming page with featured events and navigation options.
- **Contact Page**: Share feedback or get in touch with the team.
- **Responsive Design**: Accessible on desktop and mobile devices.
- **Vibrant Theme**: Colorful Kenyan heritage design with a live concert background and a cultural icon.

## Tech Stack
- **Backend**: Flask, Flask-CORS, Supabase (Python 3.x)
- **Frontend**: React with Tailwind CSS, built using Meku.dev for web app development
- **Database**: Supabase for event storage
- **Hosting**: Render for backend
- **Development**: Git and GitHub

## Installation
### Prerequisites
- Python 3.x
- Node.js and npm
- Git

### Steps
1. **Clone the Repository**: Download the project files to your computer.
2. **Set Up Backend**: Install required dependencies (`pip install flask flask-cors python-dotenv supabase`) and configure `.env` with `SUPABASE_URL` and `SUPABASE_KEY`.
3. **Set Up Frontend**: Install frontend dependencies and start the development server.
   - Follow the folder structure in the repository for specific setup instructions.

## Usage
- **Add an Event**: Use the "Add Event" form to input and submit event details.
- **Browse Events**: Explore events and use the filters or search to refine results.
- **View Homepage**: Check out featured events and navigate the site.
- **Contact**: Visit the "Contact" page to send messages or find contact information.

## API Endpoints
- **GET /view_events**: Retrieve a list of all events from Supabase.
- **POST /add_event**: Submit a new event with required details to Supabase.

## Deployment
- **Backend**: Hosted on Render with automatic updates from GitHub.
- **Frontend**: Built with Meku.dev and deployed directly on its platform for a seamless live experience.

## Contributing
1. Fork the repository to create your own copy.
2. Create a new branch for your changes.
3. Commit your updates with a descriptive message.
4. Push your branch and open a Pull Request for review.

## License
This project is released under the MIT License.

## Contact
- Email: brendachebet2030@gmail.com
- GitHub: [bree-byte](https://github.com/bree-byte)
