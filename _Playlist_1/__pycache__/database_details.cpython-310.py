o
    -TTfR  �                   @   s   d dl Z G dd� d�ZdS )�    Nc                   @   sD   e Zd Zdd� Zedd� �Zedd� �Zedd� �Zed	d
� �ZdS )�DataBaseDetailsc                 C   s@   t jjddd�| _t j�d�| _t j�d�| _t j�d�| _d S )NZdb_host�	localhost)�defaultZdb_user�databaseZdb_password)�os�environ�get�_DataBaseDetails__host�_DataBaseDetails__user�_DataBaseDetails__database�_DataBaseDetails__password��self� r   �7C:\Users\billau\Desktop\ecommerce_1\database_details.py�__init__   s   zDataBaseDetails.__init__c                 C   �   | j S �N)r   r   r   r   r   �get_password   �   zDataBaseDetails.get_passwordc                 C   r   r   )r	   r   r   r   r   �get_host   r   zDataBaseDetails.get_hostc                 C   r   r   )r
   r   r   r   r   �get_user   r   zDataBaseDetails.get_userc                 C   r   r   )r   r   r   r   r   �get_database   r   zDataBaseDetails.get_databaseN)	�__name__�
__module__�__qualname__r   �propertyr   r   r   r   r   r   r   r   r      s    


r   )r   r   r   r   r   r   �<module>   s    