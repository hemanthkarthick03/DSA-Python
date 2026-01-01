# React Cheatsheet - Complete Guide with Best Practices

## Table of Contents
- [Setup & Installation](#setup--installation)
- [Components](#components)
- [JSX](#jsx)
- [Props & State](#props--state)
- [Hooks](#hooks)
- [Event Handling](#event-handling)
- [Conditional Rendering](#conditional-rendering)
- [Lists & Keys](#lists--keys)
- [Forms](#forms)
- [Context API](#context-api)
- [Error Boundaries](#error-boundaries)
- [Performance Optimization](#performance-optimization)
- [Testing](#testing)
- [Best Practices](#best-practices)
- [Real-World Patterns](#real-world-patterns)
- [Production Tips](#production-tips)

## Setup & Installation

### Create React App
```bash
# Create new app
npx create-react-app my-app
cd my-app
npm start

# With TypeScript
npx create-react-app my-app --template typescript

# With specific React version
npx create-react-app@latest my-app
```

### Vite (Faster Alternative)
```bash
# Create with Vite
npm create vite@latest my-app -- --template react
cd my-app
npm install
npm run dev

# With TypeScript
npm create vite@latest my-app -- --template react-ts
```

### Essential Dependencies
```bash
# Routing
npm install react-router-dom

# State Management
npm install @reduxjs/toolkit react-redux
npm install zustand

# HTTP Client
npm install axios
npm install @tanstack/react-query

# UI Libraries
npm install @mui/material @emotion/react @emotion/styled
npm install antd
npm install react-bootstrap bootstrap

# Forms
npm install react-hook-form
npm install formik yup

# Utilities
npm install lodash
npm install date-fns
npm install classnames
```

## Components

### Functional Components
```jsx
// Basic functional component
const Welcome = () => {
  return <h1>Hello, World!</h1>;
};

// With props
const Greeting = ({ name, age }) => {
  return (
    <div>
      <h1>Hello, {name}!</h1>
      <p>You are {age} years old.</p>
    </div>
  );
};

// With TypeScript
interface GreetingProps {
  name: string;
  age: number;
  isActive?: boolean;
}

const Greeting: React.FC<GreetingProps> = ({ name, age, isActive = false }) => {
  return (
    <div>
      <h1>Hello, {name}!</h1>
      <p>You are {age} years old.</p>
      {isActive && <span>Active</span>}
    </div>
  );
};
```

### Component Composition
```jsx
// Higher-Order Component (HOC)
const withLoading = (WrappedComponent) => {
  return function WithLoadingComponent({ isLoading, ...props }) {
    if (isLoading) {
      return <div>Loading...</div>;
    }
    return <WrappedComponent {...props} />;
  };
};

// Usage
const EnhancedComponent = withLoading(MyComponent);

// Render Props Pattern
const DataFetcher = ({ children }) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchData().then(result => {
      setData(result);
      setLoading(false);
    });
  }, []);

  return children({ data, loading });
};

// Usage
<DataFetcher>
  {({ data, loading }) => (
    loading ? <Spinner /> : <DataDisplay data={data} />
  )}
</DataFetcher>
```

## JSX

### Basic Syntax
```jsx
// JSX expressions
const element = <h1>Hello, {name}!</h1>;

// Multi-line JSX
const element = (
  <div>
    <h1>Hello!</h1>
    <p>Welcome to React</p>
  </div>
);

// Fragments
const element = (
  <>
    <h1>Title</h1>
    <p>Description</p>
  </>
);

// Or explicit Fragment
const element = (
  <React.Fragment>
    <h1>Title</h1>
    <p>Description</p>
  </React.Fragment>
);
```

### JSX Attributes
```jsx
// String attributes
<img src="image.jpg" alt="Description" />

// Expression attributes
<img src={imageUrl} alt={imageAlt} />

// Boolean attributes
<input disabled />
<input disabled={true} />
<input disabled={isDisabled} />

// CSS classes
<div className="container" />
<div className={`container ${isActive ? 'active' : ''}`} />

// Inline styles
<div style={{ color: 'red', fontSize: '16px' }} />
```

## Props & State

### Props
```jsx
// Default props
const Button = ({ text = 'Click me', onClick, variant = 'primary' }) => {
  return (
    <button className={`btn btn-${variant}`} onClick={onClick}>
      {text}
    </button>
  );
};

// Props validation with PropTypes
import PropTypes from 'prop-types';

Button.propTypes = {
  text: PropTypes.string,
  onClick: PropTypes.func.isRequired,
  variant: PropTypes.oneOf(['primary', 'secondary', 'danger'])
};

// TypeScript interface
interface ButtonProps {
  text?: string;
  onClick: () => void;
  variant?: 'primary' | 'secondary' | 'danger';
  children?: React.ReactNode;
}

const Button: React.FC<ButtonProps> = ({ 
  text = 'Click me', 
  onClick, 
  variant = 'primary',
  children 
}) => {
  return (
    <button className={`btn btn-${variant}`} onClick={onClick}>
      {children || text}
    </button>
  );
};
```

### State with useState
```jsx
import { useState } from 'react';

// Basic state
const Counter = () => {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <button onClick={() => setCount(prev => prev - 1)}>Decrement</button>
    </div>
  );
};

// Object state
const UserForm = () => {
  const [user, setUser] = useState({
    name: '',
    email: '',
    age: 0
  });

  const updateUser = (field, value) => {
    setUser(prev => ({
      ...prev,
      [field]: value
    }));
  };

  return (
    <form>
      <input 
        value={user.name}
        onChange={(e) => updateUser('name', e.target.value)}
        placeholder="Name"
      />
      <input 
        value={user.email}
        onChange={(e) => updateUser('email', e.target.value)}
        placeholder="Email"
      />
    </form>
  );
};

// Array state
const TodoList = () => {
  const [todos, setTodos] = useState([]);

  const addTodo = (text) => {
    setTodos(prev => [...prev, { id: Date.now(), text, completed: false }]);
  };

  const toggleTodo = (id) => {
    setTodos(prev => 
      prev.map(todo => 
        todo.id === id ? { ...todo, completed: !todo.completed } : todo
      )
    );
  };

  const removeTodo = (id) => {
    setTodos(prev => prev.filter(todo => todo.id !== id));
  };

  return (
    <div>
      {todos.map(todo => (
        <div key={todo.id}>
          <span 
            style={{ textDecoration: todo.completed ? 'line-through' : 'none' }}
            onClick={() => toggleTodo(todo.id)}
          >
            {todo.text}
          </span>
          <button onClick={() => removeTodo(todo.id)}>Delete</button>
        </div>
      ))}
    </div>
  );
};
```

## Hooks

### useEffect
```jsx
import { useState, useEffect } from 'react';

// Basic effect
const DataComponent = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetchData().then(setData);
  }, []); // Empty dependency array - runs once

  return <div>{data ? JSON.stringify(data) : 'Loading...'}</div>;
};

// Effect with dependencies
const UserProfile = ({ userId }) => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    if (userId) {
      fetchUser(userId).then(setUser);
    }
  }, [userId]); // Runs when userId changes

  return user ? <div>{user.name}</div> : <div>Loading...</div>;
};

// Effect with cleanup
const Timer = () => {
  const [seconds, setSeconds] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setSeconds(prev => prev + 1);
    }, 1000);

    return () => clearInterval(interval); // Cleanup
  }, []);

  return <div>Seconds: {seconds}</div>;
};

// Multiple effects
const Component = () => {
  useEffect(() => {
    // Effect 1: Document title
    document.title = 'My App';
  }, []);

  useEffect(() => {
    // Effect 2: Event listener
    const handleResize = () => console.log('Resized');
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  return <div>Component</div>;
};
```

### Custom Hooks
```jsx
// Custom hook for API calls
const useApi = (url) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const response = await fetch(url);
        const result = await response.json();
        setData(result);
      } catch (err) {
        setError(err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [url]);

  return { data, loading, error };
};

// Usage
const UserList = () => {
  const { data: users, loading, error } = useApi('/api/users');

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
};

// Custom hook for local storage
const useLocalStorage = (key, initialValue) => {
  const [storedValue, setStoredValue] = useState(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      return initialValue;
    }
  });

  const setValue = (value) => {
    try {
      setStoredValue(value);
      window.localStorage.setItem(key, JSON.stringify(value));
    } catch (error) {
      console.error(error);
    }
  };

  return [storedValue, setValue];
};

// Custom hook for debouncing
const useDebounce = (value, delay) => {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => {
      clearTimeout(handler);
    };
  }, [value, delay]);

  return debouncedValue;
};

// Usage
const SearchComponent = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const debouncedSearchTerm = useDebounce(searchTerm, 300);

  useEffect(() => {
    if (debouncedSearchTerm) {
      // Perform search
      console.log('Searching for:', debouncedSearchTerm);
    }
  }, [debouncedSearchTerm]);

  return (
    <input
      value={searchTerm}
      onChange={(e) => setSearchTerm(e.target.value)}
      placeholder="Search..."
    />
  );
};
```

### Other Important Hooks
```jsx
import { 
  useContext, 
  useReducer, 
  useMemo, 
  useCallback, 
  useRef,
  useImperativeHandle,
  forwardRef
} from 'react';

// useReducer for complex state
const initialState = { count: 0 };

const reducer = (state, action) => {
  switch (action.type) {
    case 'increment':
      return { count: state.count + 1 };
    case 'decrement':
      return { count: state.count - 1 };
    case 'reset':
      return initialState;
    default:
      throw new Error();
  }
};

const Counter = () => {
  const [state, dispatch] = useReducer(reducer, initialState);

  return (
    <div>
      Count: {state.count}
      <button onClick={() => dispatch({ type: 'increment' })}>+</button>
      <button onClick={() => dispatch({ type: 'decrement' })}>-</button>
      <button onClick={() => dispatch({ type: 'reset' })}>Reset</button>
    </div>
  );
};

// useMemo for expensive calculations
const ExpensiveComponent = ({ items }) => {
  const expensiveValue = useMemo(() => {
    return items.reduce((sum, item) => sum + item.value, 0);
  }, [items]);

  return <div>Total: {expensiveValue}</div>;
};

// useCallback for function memoization
const Parent = () => {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');

  const handleClick = useCallback(() => {
    setCount(prev => prev + 1);
  }, []); // Function doesn't change

  return (
    <div>
      <input value={name} onChange={(e) => setName(e.target.value)} />
      <Child onClick={handleClick} />
      <div>Count: {count}</div>
    </div>
  );
};

// useRef for DOM access and mutable values
const FocusInput = () => {
  const inputRef = useRef(null);

  const focusInput = () => {
    inputRef.current.focus();
  };

  return (
    <div>
      <input ref={inputRef} />
      <button onClick={focusInput}>Focus Input</button>
    </div>
  );
};

// Forward ref
const FancyButton = forwardRef((props, ref) => (
  <button ref={ref} className="fancy-button">
    {props.children}
  </button>
));
```

## Event Handling

### Basic Events
```jsx
const EventExample = () => {
  const handleClick = (e) => {
    e.preventDefault();
    console.log('Button clicked');
  };

  const handleChange = (e) => {
    console.log('Input value:', e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    console.log('Form data:', Object.fromEntries(formData));
  };

  return (
    <form onSubmit={handleSubmit}>
      <input onChange={handleChange} name="username" />
      <button onClick={handleClick}>Submit</button>
    </form>
  );
};

// Event with parameters
const ListComponent = () => {
  const items = ['Item 1', 'Item 2', 'Item 3'];

  const handleItemClick = (item, index) => {
    console.log(`Clicked ${item} at index ${index}`);
  };

  return (
    <ul>
      {items.map((item, index) => (
        <li 
          key={index}
          onClick={() => handleItemClick(item, index)}
        >
          {item}
        </li>
      ))}
    </ul>
  );
};
```

## Conditional Rendering

```jsx
const ConditionalExample = ({ user, isLoading, error }) => {
  // If-else with ternary
  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div>
      {/* Conditional rendering with && */}
      {user && <h1>Welcome, {user.name}!</h1>}
      
      {/* Ternary operator */}
      {user ? (
        <div>
          <p>Email: {user.email}</p>
          <p>Role: {user.role}</p>
        </div>
      ) : (
        <div>Please log in</div>
      )}

      {/* Multiple conditions */}
      {user && user.role === 'admin' && (
        <button>Admin Panel</button>
      )}

      {/* Switch-like rendering */}
      {(() => {
        switch (user?.role) {
          case 'admin':
            return <AdminPanel />;
          case 'user':
            return <UserPanel />;
          default:
            return <GuestPanel />;
        }
      })()}
    </div>
  );
};
```

## Lists & Keys

```jsx
const ListExample = () => {
  const users = [
    { id: 1, name: 'John', email: 'john@example.com' },
    { id: 2, name: 'Jane', email: 'jane@example.com' },
    { id: 3, name: 'Bob', email: 'bob@example.com' }
  ];

  return (
    <div>
      {/* Basic list */}
      <ul>
        {users.map(user => (
          <li key={user.id}>
            {user.name} - {user.email}
          </li>
        ))}
      </ul>

      {/* List with components */}
      <div>
        {users.map(user => (
          <UserCard key={user.id} user={user} />
        ))}
      </div>

      {/* List with index (avoid if possible) */}
      <ul>
        {users.map((user, index) => (
          <li key={`user-${index}`}>
            {user.name}
          </li>
        ))}
      </ul>
    </div>
  );
};

const UserCard = ({ user }) => (
  <div className="user-card">
    <h3>{user.name}</h3>
    <p>{user.email}</p>
  </div>
);
```

## Forms

### Controlled Components
```jsx
const ContactForm = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: '',
    category: 'general',
    subscribe: false
  });

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Form submitted:', formData);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        name="name"
        value={formData.name}
        onChange={handleChange}
        placeholder="Name"
        required
      />
      
      <input
        type="email"
        name="email"
        value={formData.email}
        onChange={handleChange}
        placeholder="Email"
        required
      />
      
      <textarea
        name="message"
        value={formData.message}
        onChange={handleChange}
        placeholder="Message"
        rows={4}
      />
      
      <select
        name="category"
        value={formData.category}
        onChange={handleChange}
      >
        <option value="general">General</option>
        <option value="support">Support</option>
        <option value="sales">Sales</option>
      </select>
      
      <label>
        <input
          type="checkbox"
          name="subscribe"
          checked={formData.subscribe}
          onChange={handleChange}
        />
        Subscribe to newsletter
      </label>
      
      <button type="submit">Submit</button>
    </form>
  );
};
```

### React Hook Form (Recommended)
```jsx
import { useForm } from 'react-hook-form';

const HookForm = () => {
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors, isSubmitting }
  } = useForm();

  const onSubmit = async (data) => {
    await new Promise(resolve => setTimeout(resolve, 1000));
    console.log(data);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input
        {...register('name', { 
          required: 'Name is required',
          minLength: { value: 2, message: 'Name must be at least 2 characters' }
        })}
        placeholder="Name"
      />
      {errors.name && <span>{errors.name.message}</span>}

      <input
        {...register('email', {
          required: 'Email is required',
          pattern: {
            value: /^\S+@\S+$/i,
            message: 'Invalid email address'
          }
        })}
        placeholder="Email"
      />
      {errors.email && <span>{errors.email.message}</span>}

      <button type="submit" disabled={isSubmitting}>
        {isSubmitting ? 'Submitting...' : 'Submit'}
      </button>
    </form>
  );
};
```

## Context API

```jsx
import { createContext, useContext, useReducer } from 'react';

// Create context
const AuthContext = createContext();

// Auth reducer
const authReducer = (state, action) => {
  switch (action.type) {
    case 'LOGIN':
      return { ...state, user: action.payload, isAuthenticated: true };
    case 'LOGOUT':
      return { ...state, user: null, isAuthenticated: false };
    case 'SET_LOADING':
      return { ...state, loading: action.payload };
    default:
      return state;
  }
};

// Auth provider
export const AuthProvider = ({ children }) => {
  const [state, dispatch] = useReducer(authReducer, {
    user: null,
    isAuthenticated: false,
    loading: false
  });

  const login = async (credentials) => {
    dispatch({ type: 'SET_LOADING', payload: true });
    try {
      const user = await authService.login(credentials);
      dispatch({ type: 'LOGIN', payload: user });
    } catch (error) {
      console.error('Login failed:', error);
    } finally {
      dispatch({ type: 'SET_LOADING', payload: false });
    }
  };

  const logout = () => {
    authService.logout();
    dispatch({ type: 'LOGOUT' });
  };

  const value = {
    ...state,
    login,
    logout
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
};

// Custom hook to use auth context
export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

// Usage in component
const LoginButton = () => {
  const { login, logout, isAuthenticated, loading } = useAuth();

  if (loading) return <div>Loading...</div>;

  return isAuthenticated ? (
    <button onClick={logout}>Logout</button>
  ) : (
    <button onClick={() => login({ email: 'user@example.com', password: 'password' })}>
      Login
    </button>
  );
};

// App component
const App = () => {
  return (
    <AuthProvider>
      <div>
        <LoginButton />
      </div>
    </AuthProvider>
  );
};
```

## Error Boundaries

```jsx
import { Component } from 'react';

class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null, errorInfo: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    this.setState({
      error: error,
      errorInfo: errorInfo
    });
    
    // Log error to service
    console.error('Error caught by boundary:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="error-boundary">
          <h2>Something went wrong.</h2>
          <details style={{ whiteSpace: 'pre-wrap' }}>
            {this.state.error && this.state.error.toString()}
            <br />
            {this.state.errorInfo.componentStack}
          </details>
        </div>
      );
    }

    return this.props.children;
  }
}

// Usage
const App = () => {
  return (
    <ErrorBoundary>
      <Header />
      <MainContent />
      <Footer />
    </ErrorBoundary>
  );
};

// React 18+ with react-error-boundary library
import { ErrorBoundary } from 'react-error-boundary';

function ErrorFallback({ error, resetErrorBoundary }) {
  return (
    <div role="alert">
      <h2>Something went wrong:</h2>
      <pre>{error.message}</pre>
      <button onClick={resetErrorBoundary}>Try again</button>
    </div>
  );
}

const App = () => {
  return (
    <ErrorBoundary
      FallbackComponent={ErrorFallback}
      onError={(error, errorInfo) => {
        console.error('Error logged:', error, errorInfo);
      }}
    >
      <MyApp />
    </ErrorBoundary>
  );
};
```

## Performance Optimization

### React.memo
```jsx
import { memo } from 'react';

// Memoize component to prevent unnecessary re-renders
const ExpensiveComponent = memo(({ data, onUpdate }) => {
  console.log('ExpensiveComponent rendered');
  
  return (
    <div>
      {data.map(item => (
        <div key={item.id}>{item.name}</div>
      ))}
    </div>
  );
});

// Custom comparison function
const MyComponent = memo(({ user, settings }) => {
  return <div>{user.name}</div>;
}, (prevProps, nextProps) => {
  // Return true if props are equal (skip re-render)
  return prevProps.user.id === nextProps.user.id;
});
```

### useMemo and useCallback
```jsx
const OptimizedComponent = ({ items, filter, onItemClick }) => {
  // Memoize expensive calculations
  const filteredItems = useMemo(() => {
    console.log('Filtering items...');
    return items.filter(item => item.name.includes(filter));
  }, [items, filter]);

  const sortedItems = useMemo(() => {
    console.log('Sorting items...');
    return [...filteredItems].sort((a, b) => a.name.localeCompare(b.name));
  }, [filteredItems]);

  // Memoize callback functions
  const handleItemClick = useCallback((item) => {
    onItemClick(item.id);
  }, [onItemClick]);

  return (
    <div>
      {sortedItems.map(item => (
        <ItemComponent
          key={item.id}
          item={item}
          onClick={handleItemClick}
        />
      ))}
    </div>
  );
};

const ItemComponent = memo(({ item, onClick }) => {
  return (
    <div onClick={() => onClick(item)}>
      {item.name}
    </div>
  );
});
```

### Code Splitting
```jsx
import { lazy, Suspense } from 'react';

// Lazy load components
const LazyComponent = lazy(() => import('./LazyComponent'));
const AdminPanel = lazy(() => import('./AdminPanel'));

const App = () => {
  return (
    <div>
      <Suspense fallback={<div>Loading...</div>}>
        <LazyComponent />
      </Suspense>
      
      <Suspense fallback={<div>Loading admin panel...</div>}>
        <AdminPanel />
      </Suspense>
    </div>
  );
};

// Route-based code splitting with React Router
import { Routes, Route } from 'react-router-dom';

const Home = lazy(() => import('./pages/Home'));
const About = lazy(() => import('./pages/About'));
const Contact = lazy(() => import('./pages/Contact'));

const App = () => {
  return (
    <Suspense fallback={<div>Loading page...</div>}>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </Suspense>
  );
};
```

## Testing

### Jest and React Testing Library
```jsx
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import '@testing-library/jest-dom';

// Component to test
const Counter = ({ initialCount = 0 }) => {
  const [count, setCount] = useState(initialCount);

  return (
    <div>
      <span data-testid="count">Count: {count}</span>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <button onClick={() => setCount(count - 1)}>Decrement</button>
    </div>
  );
};

// Tests
describe('Counter Component', () => {
  test('renders initial count', () => {
    render(<Counter initialCount={5} />);
    expect(screen.getByTestId('count')).toHaveTextContent('Count: 5');
  });

  test('increments count when increment button is clicked', async () => {
    const user = userEvent.setup();
    render(<Counter />);
    
    const incrementButton = screen.getByText('Increment');
    await user.click(incrementButton);
    
    expect(screen.getByTestId('count')).toHaveTextContent('Count: 1');
  });

  test('decrements count when decrement button is clicked', () => {
    render(<Counter initialCount={5} />);
    
    fireEvent.click(screen.getByText('Decrement'));
    
    expect(screen.getByTestId('count')).toHaveTextContent('Count: 4');
  });
});

// Testing async operations
const AsyncComponent = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  const fetchData = async () => {
    setLoading(true);
    const response = await fetch('/api/data');
    const result = await response.json();
    setData(result);
    setLoading(false);
  };

  return (
    <div>
      <button onClick={fetchData}>Fetch Data</button>
      {loading && <div>Loading...</div>}
      {data && <div data-testid="data">{data.message}</div>}
    </div>
  );
};

// Mock fetch
global.fetch = jest.fn();

test('fetches and displays data', async () => {
  fetch.mockResolvedValueOnce({
    json: async () => ({ message: 'Hello World' })
  });

  render(<AsyncComponent />);
  
  fireEvent.click(screen.getByText('Fetch Data'));
  
  expect(screen.getByText('Loading...')).toBeInTheDocument();
  
  await waitFor(() => {
    expect(screen.getByTestId('data')).toHaveTextContent('Hello World');
  });
});
```

## Best Practices

### Component Structure
```jsx
// Good component structure
import React, { useState, useEffect, useCallback } from 'react';
import PropTypes from 'prop-types';
import './UserProfile.css';

// Constants
const DEFAULT_AVATAR = '/images/default-avatar.png';

// Helper functions
const formatDate = (date) => {
  return new Intl.DateTimeFormat('en-US').format(new Date(date));
};

// Main component
const UserProfile = ({ 
  userId, 
  onUpdate, 
  showActions = true,
  className = '' 
}) => {
  // State
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Effects
  useEffect(() => {
    fetchUser(userId);
  }, [userId]);

  // Handlers
  const fetchUser = useCallback(async (id) => {
    try {
      setLoading(true);
      setError(null);
      const userData = await userService.getUser(id);
      setUser(userData);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, []);

  const handleUpdate = useCallback((updatedData) => {
    setUser(prev => ({ ...prev, ...updatedData }));
    onUpdate?.(updatedData);
  }, [onUpdate]);

  // Early returns
  if (loading) return <LoadingSpinner />;
  if (error) return <ErrorMessage message={error} />;
  if (!user) return <div>User not found</div>;

  // Render
  return (
    <div className={`user-profile ${className}`}>
      <div className="user-profile__header">
        <img 
          src={user.avatar || DEFAULT_AVATAR} 
          alt={`${user.name}'s avatar`}
          className="user-profile__avatar"
        />
        <div className="user-profile__info">
          <h2 className="user-profile__name">{user.name}</h2>
          <p className="user-profile__email">{user.email}</p>
          <p className="user-profile__joined">
            Joined {formatDate(user.createdAt)}
          </p>
        </div>
      </div>
      
      {showActions && (
        <div className="user-profile__actions">
          <button onClick={() => handleUpdate({ lastSeen: new Date() })}>
            Update Last Seen
          </button>
        </div>
      )}
    </div>
  );
};

// PropTypes
UserProfile.propTypes = {
  userId: PropTypes.string.isRequired,
  onUpdate: PropTypes.func,
  showActions: PropTypes.bool,
  className: PropTypes.string
};

export default UserProfile;
```

### Folder Structure
```
src/
├── components/           # Reusable components
│   ├── common/          # Generic components
│   │   ├── Button/
│   │   ├── Modal/
│   │   └── LoadingSpinner/
│   └── forms/           # Form-specific components
├── pages/               # Page components
├── hooks/               # Custom hooks
├── services/            # API services
├── utils/               # Utility functions
├── contexts/            # React contexts
├── constants/           # App constants
├── types/               # TypeScript types
└── styles/              # Global styles
```

## Real-World Patterns

### Data Fetching Pattern
```jsx
// Custom hook for data fetching
const useApiData = (url, options = {}) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchData = useCallback(async () => {
    try {
      setLoading(true);
      setError(null);
      const response = await fetch(url, options);
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const result = await response.json();
      setData(result);
    } catch (err) {
      setError(err);
    } finally {
      setLoading(false);
    }
  }, [url, JSON.stringify(options)]);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  return { data, loading, error, refetch: fetchData };
};

// Usage with error handling and retry
const UserList = () => {
  const { data: users, loading, error, refetch } = useApiData('/api/users');

  if (loading) return <LoadingSpinner />;
  
  if (error) {
    return (
      <ErrorBoundary>
        <div className="error-state">
          <p>Failed to load users: {error.message}</p>
          <button onClick={refetch}>Retry</button>
        </div>
      </ErrorBoundary>
    );
  }

  return (
    <div className="user-list">
      {users?.map(user => (
        <UserCard key={user.id} user={user} />
      ))}
    </div>
  );
};
```

### Form Validation Pattern
```jsx
// Custom validation hook
const useFormValidation = (initialValues, validationRules) => {
  const [values, setValues] = useState(initialValues);
  const [errors, setErrors] = useState({});
  const [touched, setTouched] = useState({});

  const validate = useCallback((fieldName, value) => {
    const rule = validationRules[fieldName];
    if (!rule) return '';

    if (rule.required && !value) {
      return rule.required;
    }

    if (rule.minLength && value.length < rule.minLength.value) {
      return rule.minLength.message;
    }

    if (rule.pattern && !rule.pattern.value.test(value)) {
      return rule.pattern.message;
    }

    return '';
  }, [validationRules]);

  const handleChange = (name, value) => {
    setValues(prev => ({ ...prev, [name]: value }));
    
    if (touched[name]) {
      const error = validate(name, value);
      setErrors(prev => ({ ...prev, [name]: error }));
    }
  };

  const handleBlur = (name) => {
    setTouched(prev => ({ ...prev, [name]: true }));
    const error = validate(name, values[name]);
    setErrors(prev => ({ ...prev, [name]: error }));
  };

  const validateAll = () => {
    const newErrors = {};
    Object.keys(validationRules).forEach(field => {
      newErrors[field] = validate(field, values[field]);
    });
    setErrors(newErrors);
    setTouched(Object.keys(validationRules).reduce((acc, key) => {
      acc[key] = true;
      return acc;
    }, {}));
    
    return Object.values(newErrors).every(error => !error);
  };

  return {
    values,
    errors,
    touched,
    handleChange,
    handleBlur,
    validateAll,
    isValid: Object.values(errors).every(error => !error)
  };
};

// Usage
const ContactForm = () => {
  const validationRules = {
    name: {
      required: 'Name is required',
      minLength: { value: 2, message: 'Name must be at least 2 characters' }
    },
    email: {
      required: 'Email is required',
      pattern: {
        value: /^\S+@\S+\.\S+$/,
        message: 'Please enter a valid email'
      }
    }
  };

  const {
    values,
    errors,
    touched,
    handleChange,
    handleBlur,
    validateAll,
    isValid
  } = useFormValidation({ name: '', email: '' }, validationRules);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (validateAll()) {
      console.log('Form submitted:', values);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="form-field">
        <input
          type="text"
          value={values.name}
          onChange={(e) => handleChange('name', e.target.value)}
          onBlur={() => handleBlur('name')}
          placeholder="Name"
          className={errors.name && touched.name ? 'error' : ''}
        />
        {errors.name && touched.name && (
          <span className="error-message">{errors.name}</span>
        )}
      </div>

      <div className="form-field">
        <input
          type="email"
          value={values.email}
          onChange={(e) => handleChange('email', e.target.value)}
          onBlur={() => handleBlur('email')}
          placeholder="Email"
          className={errors.email && touched.email ? 'error' : ''}
        />
        {errors.email && touched.email && (
          <span className="error-message">{errors.email}</span>
        )}
      </div>

      <button type="submit" disabled={!isValid}>
        Submit
      </button>
    </form>
  );
};
```

### Modal Management Pattern
```jsx
// Modal context
const ModalContext = createContext();

export const ModalProvider = ({ children }) => {
  const [modals, setModals] = useState([]);

  const openModal = (component, props = {}) => {
    const id = Date.now().toString();
    setModals(prev => [...prev, { id, component, props }]);
    return id;
  };

  const closeModal = (id) => {
    setModals(prev => prev.filter(modal => modal.id !== id));
  };

  const closeAllModals = () => {
    setModals([]);
  };

  return (
    <ModalContext.Provider value={{ openModal, closeModal, closeAllModals }}>
      {children}
      {modals.map(({ id, component: Component, props }) => (
        <Component key={id} onClose={() => closeModal(id)} {...props} />
      ))}
    </ModalContext.Provider>
  );
};

export const useModal = () => {
  const context = useContext(ModalContext);
  if (!context) {
    throw new Error('useModal must be used within ModalProvider');
  }
  return context;
};

// Usage
const MyComponent = () => {
  const { openModal } = useModal();

  const handleOpenConfirm = () => {
    openModal(ConfirmDialog, {
      title: 'Delete Item',
      message: 'Are you sure you want to delete this item?',
      onConfirm: () => console.log('Confirmed'),
      onCancel: () => console.log('Cancelled')
    });
  };

  return <button onClick={handleOpenConfirm}>Delete</button>;
};
```

## Production Tips

### Environment Configuration
```jsx
// config/environment.js
const config = {
  development: {
    API_URL: 'http://localhost:3001/api',
    DEBUG: true,
    LOG_LEVEL: 'debug'
  },
  production: {
    API_URL: 'https://api.myapp.com',
    DEBUG: false,
    LOG_LEVEL: 'error'
  },
  test: {
    API_URL: 'http://localhost:3001/api',
    DEBUG: false,
    LOG_LEVEL: 'silent'
  }
};

export default config[process.env.NODE_ENV || 'development'];

// Usage
import config from './config/environment';

const apiService = {
  baseURL: config.API_URL,
  
  async get(endpoint) {
    const response = await fetch(`${this.baseURL}${endpoint}`);
    if (config.DEBUG) {
      console.log('API Response:', response);
    }
    return response.json();
  }
};
```

### Error Logging
```jsx
// utils/errorLogger.js
class ErrorLogger {
  static log(error, context = {}) {
    const errorInfo = {
      message: error.message,
      stack: error.stack,
      timestamp: new Date().toISOString(),
      url: window.location.href,
      userAgent: navigator.userAgent,
      ...context
    };

    if (process.env.NODE_ENV === 'production') {
      // Send to logging service
      this.sendToLoggingService(errorInfo);
    } else {
      console.error('Error logged:', errorInfo);
    }
  }

  static sendToLoggingService(errorInfo) {
    fetch('/api/errors', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(errorInfo)
    }).catch(err => console.error('Failed to log error:', err));
  }
}

// Global error handler
window.addEventListener('error', (event) => {
  ErrorLogger.log(event.error, {
    type: 'javascript_error',
    filename: event.filename,
    lineno: event.lineno,
    colno: event.colno
  });
});

window.addEventListener('unhandledrejection', (event) => {
  ErrorLogger.log(new Error(event.reason), {
    type: 'unhandled_promise_rejection'
  });
});

export default ErrorLogger;
```

### Performance Monitoring
```jsx
// utils/performance.js
class PerformanceMonitor {
  static measureComponent(WrappedComponent, componentName) {
    return function MeasuredComponent(props) {
      useEffect(() => {
        const startTime = performance.now();
        
        return () => {
          const endTime = performance.now();
          const renderTime = endTime - startTime;
          
          if (renderTime > 16) { // Longer than one frame
            console.warn(`${componentName} took ${renderTime}ms to render`);
          }
        };
      });

      return <WrappedComponent {...props} />;
    };
  }

  static measureFunction(fn, name) {
    return function(...args) {
      const start = performance.now();
      const result = fn.apply(this, args);
      const end = performance.now();
      
      console.log(`${name} took ${end - start}ms`);
      return result;
    };
  }
}

// Usage
const ExpensiveComponent = PerformanceMonitor.measureComponent(
  MyExpensiveComponent,
  'MyExpensiveComponent'
);
```

### Bundle Analysis
```bash
# Analyze bundle size
npm install --save-dev webpack-bundle-analyzer

# Add to package.json scripts
"analyze": "npm run build && npx webpack-bundle-analyzer build/static/js/*.js"

# Run analysis
npm run analyze
```

### Security Best Practices
```jsx
// Sanitize user input
import DOMPurify from 'dompurify';

const SafeHTML = ({ html }) => {
  const sanitizedHTML = DOMPurify.sanitize(html);
  return <div dangerouslySetInnerHTML={{ __html: sanitizedHTML }} />;
};

// Secure API calls
const secureApiCall = async (endpoint, options = {}) => {
  const token = localStorage.getItem('authToken');
  
  const config = {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`,
      'X-Requested-With': 'XMLHttpRequest', // CSRF protection
      ...options.headers
    }
  };

  const response = await fetch(endpoint, config);
  
  if (response.status === 401) {
    // Handle unauthorized
    localStorage.removeItem('authToken');
    window.location.href = '/login';
  }
  
  return response;
};

// Content Security Policy
// Add to index.html
<meta http-equiv="Content-Security-Policy" 
      content="default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline';">
```

This comprehensive React cheatsheet covers everything from basic concepts to advanced patterns used in production applications. Keep it handy for quick reference and best practices!