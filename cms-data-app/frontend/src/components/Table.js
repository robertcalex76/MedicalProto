import React, { useEffect, useState } from 'react';

const Table = () => {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch('/api/nursing-homes');
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const result = await response.json();
                setData(result);
            } catch (error) {
                setError(error);
            } finally {
                setLoading(false);
            }
        };

        fetchData();
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error: {error.message}</div>;
    }

    return (
        <table>
            <thead>
                <tr>
                    <th>Provider Name</th>
                    <th>Address</th>
                    <th>Rating</th>
                    <th>Staffing</th>
                    <th>Violations</th>
                </tr>
            </thead>
            <tbody>
                {data.map((facility) => (
                    <tr key={facility.id}>
                        <td>{facility.provider_name}</td>
                        <td>{facility.address}</td>
                        <td>{facility.rating}</td>
                        <td>{facility.staffing}</td>
                        <td>{facility.violations}</td>
                    </tr>
                ))}
            </tbody>
        </table>
    );
};

export default Table;