# user the officile Node.js image from the Docker Hub
FROM node:14

# Set the working directory in the container
WORKDIR /user/src/app

# Copy the current directory contents into the container at /user/src/app
COPY package*.json ./

# Install any needed packages specified in package.json
RUN npm install

# Copy the current directory contents into the container at /user/src/app
COPY . .

# Expose port to the outside world
EXPOSE 3000

# Run app.py when the container launches
CMD ["npm", "start"]