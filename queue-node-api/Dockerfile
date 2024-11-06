# Stage 1: Build the NestJS application
FROM node:22 AS builder

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install --legacy-peer-deps

# Copy the source code
COPY . .

# Build the NestJS app
RUN npm run build

# Stage 2: Create the production image
FROM node:22 AS runner

# Set the working directory
WORKDIR /app

# Copy only the production dependencies from the builder stage
COPY --from=builder /app/node_modules ./node_modules

# Copy the built application code
COPY --from=builder /app/dist ./dist

# Expose the application port
EXPOSE 3000

# Set environment variables
ENV NODE_ENV=production

# Run the NestJS application
CMD ["node", "dist/main"]
