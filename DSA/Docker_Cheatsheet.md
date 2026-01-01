# Docker Cheatsheet

## Table of Contents
- [Installation & Setup](#installation--setup)
- [Basic Commands](#basic-commands)
- [Image Management](#image-management)
- [Container Management](#container-management)
- [Dockerfile](#dockerfile)
- [Docker Compose](#docker-compose)
- [Networking](#networking)
- [Volumes & Data Management](#volumes--data-management)
- [Registry & Hub](#registry--hub)
- [Monitoring & Debugging](#monitoring--debugging)
- [Best Practices](#best-practices)

## Installation & Setup

### Install Docker
```bash
# Ubuntu/Debian
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Windows/Mac
# Download Docker Desktop from docker.com

# Verify installation
docker --version
docker-compose --version
```

### Post-installation setup
```bash
# Add user to docker group (Linux)
sudo usermod -aG docker $USER

# Start Docker service
sudo systemctl start docker
sudo systemctl enable docker
```

## Basic Commands

### System Information
```bash
docker version              # Show Docker version
docker info                 # Display system-wide information
docker system df            # Show Docker disk usage
docker system prune         # Remove unused data
docker system prune -a      # Remove all unused data including images
```

### Help
```bash
docker --help               # General help
docker COMMAND --help       # Command-specific help
```

## Image Management

### Building Images
```bash
docker build -t myapp:latest .                    # Build from Dockerfile
docker build -t myapp:v1.0 -f Dockerfile.prod .  # Use specific Dockerfile
docker build --no-cache -t myapp .                # Build without cache
docker build --build-arg ARG_NAME=value .         # Pass build arguments
```

### Listing Images
```bash
docker images               # List all images
docker images -a            # List all images including intermediate
docker images --filter dangling=true  # List dangling images
docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}"
```

### Managing Images
```bash
docker pull ubuntu:20.04    # Pull image from registry
docker push myapp:latest     # Push image to registry
docker tag myapp:latest myapp:v1.0  # Tag an image
docker rmi image_id          # Remove image
docker rmi $(docker images -q)  # Remove all images
docker image prune           # Remove dangling images
docker image prune -a        # Remove all unused images
```

### Image Inspection
```bash
docker inspect image_name    # Detailed image information
docker history image_name    # Show image layers
docker image ls --digests    # Show image digests
```

## Container Management

### Running Containers
```bash
docker run ubuntu                           # Run container
docker run -it ubuntu bash                  # Interactive mode with terminal
docker run -d nginx                         # Run in detached mode
docker run -p 8080:80 nginx                # Port mapping
docker run -v /host/path:/container/path ubuntu  # Volume mounting
docker run --name mycontainer ubuntu        # Name the container
docker run --rm ubuntu                      # Remove container after exit
docker run -e ENV_VAR=value ubuntu         # Set environment variables
docker run --restart=always nginx          # Restart policy
```

### Container Lifecycle
```bash
docker ps                   # List running containers
docker ps -a                # List all containers
docker start container_id   # Start stopped container
docker stop container_id    # Stop running container
docker restart container_id # Restart container
docker pause container_id   # Pause container
docker unpause container_id # Unpause container
docker kill container_id    # Force kill container
```

### Container Operations
```bash
docker exec -it container_id bash          # Execute command in running container
docker logs container_id                   # View container logs
docker logs -f container_id                # Follow log output
docker logs --tail 50 container_id         # Show last 50 lines
docker cp file.txt container_id:/path/     # Copy file to container
docker cp container_id:/path/file.txt .    # Copy file from container
```

### Container Cleanup
```bash
docker rm container_id                     # Remove container
docker rm $(docker ps -aq)                # Remove all containers
docker container prune                     # Remove all stopped containers
```

### Container Inspection
```bash
docker inspect container_id               # Detailed container info
docker stats                             # Live resource usage stats
docker stats container_id                # Stats for specific container
docker top container_id                  # Running processes in container
docker port container_id                 # Port mappings
```

## Dockerfile

### Basic Structure
```dockerfile
# Use official base image
FROM node:16-alpine

# Set working directory
WORKDIR /app

# Set environment variables
ENV NODE_ENV=production

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy application code
COPY . .

# Expose port
EXPOSE 3000

# Create non-root user
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001
USER nextjs

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:3000/health || exit 1

# Start application
CMD ["npm", "start"]
```

### Common Instructions
```dockerfile
FROM image:tag              # Base image
WORKDIR /path               # Set working directory
COPY src dest               # Copy files
ADD src dest                # Copy files (with URL/tar support)
RUN command                 # Execute command
CMD ["executable", "param"] # Default command
ENTRYPOINT ["executable"]   # Configure container executable
EXPOSE port                 # Expose port
ENV key=value              # Set environment variable
ARG key=default            # Build-time variable
VOLUME ["/data"]           # Create mount point
USER username              # Set user
LABEL key=value            # Add metadata
ONBUILD instruction        # Trigger for child images
```

### Multi-stage Build
```dockerfile
# Build stage
FROM node:16 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Production stage
FROM node:16-alpine AS production
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY package*.json ./
EXPOSE 3000
CMD ["npm", "start"]
```

## Docker Compose

### Basic docker-compose.yml
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
    volumes:
      - .:/app
      - /app/node_modules
    depends_on:
      - db
    networks:
      - app-network

  db:
    image: postgres:13
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - app-network

volumes:
  postgres_data:

networks:
  app-network:
    driver: bridge
```

### Docker Compose Commands
```bash
docker-compose up                    # Start services
docker-compose up -d                 # Start in detached mode
docker-compose up --build            # Build and start
docker-compose down                  # Stop and remove containers
docker-compose down -v               # Stop and remove volumes
docker-compose ps                    # List services
docker-compose logs                  # View logs
docker-compose logs -f service_name  # Follow logs for service
docker-compose exec service_name bash  # Execute command in service
docker-compose build                 # Build services
docker-compose pull                  # Pull service images
docker-compose restart service_name  # Restart service
docker-compose scale service_name=3  # Scale service
```

### Environment Files
```bash
# .env file
DATABASE_URL=postgresql://user:pass@db:5432/myapp
API_KEY=your_api_key_here
DEBUG=true
```

## Networking

### Network Commands
```bash
docker network ls                    # List networks
docker network create mynetwork     # Create network
docker network create --driver bridge mynetwork  # Create bridge network
docker network inspect mynetwork    # Inspect network
docker network rm mynetwork         # Remove network
docker network prune                # Remove unused networks
```

### Connect Containers
```bash
docker run --network mynetwork nginx           # Connect to network
docker network connect mynetwork container_id  # Connect running container
docker network disconnect mynetwork container_id  # Disconnect container
```

### Network Types
```bash
# Bridge (default)
docker network create --driver bridge my-bridge

# Host (use host networking)
docker run --network host nginx

# None (no networking)
docker run --network none alpine

# Overlay (for swarm)
docker network create --driver overlay my-overlay
```

## Volumes & Data Management

### Volume Commands
```bash
docker volume ls                     # List volumes
docker volume create myvolume       # Create volume
docker volume inspect myvolume      # Inspect volume
docker volume rm myvolume           # Remove volume
docker volume prune                 # Remove unused volumes
```

### Volume Types
```bash
# Named volume
docker run -v myvolume:/data nginx

# Bind mount
docker run -v /host/path:/container/path nginx

# Anonymous volume
docker run -v /container/path nginx

# Read-only mount
docker run -v /host/path:/container/path:ro nginx
```

### Backup and Restore
```bash
# Backup volume
docker run --rm -v myvolume:/data -v $(pwd):/backup alpine tar czf /backup/backup.tar.gz -C /data .

# Restore volume
docker run --rm -v myvolume:/data -v $(pwd):/backup alpine tar xzf /backup/backup.tar.gz -C /data
```

## Registry & Hub

### Docker Hub
```bash
docker login                        # Login to Docker Hub
docker logout                       # Logout
docker search ubuntu                # Search for images
docker pull ubuntu:20.04            # Pull image
docker push username/myapp:latest    # Push image
```

### Private Registry
```bash
# Run local registry
docker run -d -p 5000:5000 --name registry registry:2

# Tag for private registry
docker tag myapp localhost:5000/myapp

# Push to private registry
docker push localhost:5000/myapp

# Pull from private registry
docker pull localhost:5000/myapp
```

## Monitoring & Debugging

### Container Monitoring
```bash
docker stats                        # Live resource usage
docker stats --no-stream            # One-time stats
docker events                       # Real-time events
docker events --filter container=mycontainer  # Filter events
```

### Debugging
```bash
docker logs container_id             # View logs
docker logs --details container_id  # Detailed logs
docker exec -it container_id sh     # Interactive shell
docker inspect container_id         # Detailed info
docker diff container_id            # File changes
```

### Health Checks
```dockerfile
# In Dockerfile
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost/ || exit 1
```

```bash
docker ps                           # Shows health status
docker inspect --format='{{.State.Health.Status}}' container_id
```

## Best Practices

### Security
```dockerfile
# Use non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

# Use specific tags
FROM node:16.14.2-alpine

# Minimize layers
RUN apt-get update && apt-get install -y \
    package1 \
    package2 \
    && rm -rf /var/lib/apt/lists/*

# Use .dockerignore
# .dockerignore
node_modules
.git
.gitignore
README.md
Dockerfile
.dockerignore
```

### Performance
```dockerfile
# Order layers by change frequency
COPY package*.json ./
RUN npm ci
COPY . .

# Use multi-stage builds
FROM node:16 AS builder
# ... build steps
FROM node:16-alpine AS production
COPY --from=builder /app/dist ./dist

# Minimize image size
FROM alpine:latest
RUN apk --no-cache add ca-certificates
```

### Development
```bash
# Use bind mounts for development
docker run -v $(pwd):/app -p 3000:3000 myapp

# Use docker-compose for multi-service apps
docker-compose up --build

# Use .env files for configuration
docker run --env-file .env myapp
```

### Production
```bash
# Use restart policies
docker run --restart=unless-stopped myapp

# Set resource limits
docker run --memory=512m --cpus=1.0 myapp

# Use health checks
docker run --health-cmd="curl -f http://localhost/" myapp

# Use secrets for sensitive data
echo "mysecret" | docker secret create my_secret -
```

## Common Patterns

### Database Container
```yaml
services:
  db:
    image: postgres:13
    environment:
      POSTGRES_DB: ${DB_NAME}
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
    ports:
      - "5432:5432"
    restart: unless-stopped
```

### Web Application
```yaml
services:
  web:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "80:3000"
    environment:
      - NODE_ENV=production
    depends_on:
      - db
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
```

### Load Balancer
```yaml
services:
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - web1
      - web2
```

This cheatsheet covers the most commonly used Docker commands and patterns. Keep it handy for quick reference during development and deployment!