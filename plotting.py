import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.cluster.hierarchy import dendrogram

def plot_A_by_B(data, A='AGE', B='PLAYER_HEIGHT_INCHES'):
    """
    Plots the average value of column A by the unique values of column B.
    
    Such as plotting the average age of players by every value of height in the data.

    Parameters
    ----------
    data : pd.DataFrame
        The data to plot.
    A : str
        The column name of the data to plot on the y-axis.
    B : str
        The column name of the data to plot on the x-axis.

    Returns
    -------
    None
    """
    x = sorted(data[B].unique())
    y = [data[data[B]==i][A].mean() for i in x] 

    plt.plot(x, y, color='black')
    plt.title(A + ' by ' + B)
    plt.xlabel(B)
    plt.ylabel(A)

def plot_As_by_Bs(data, As=['AGE'], Bs=['PLAYER_HEIGHT_INCHES']):
    """Plots the average value of column A by the unique values of column B, for each pair of A and B.

    The pairs of A and B are the ones with the same index in the As and Bs lists.
    Basically, it uses the plot_A_by_B function for the zip elements of As and Bs.
    The plots are displayed in a 2-column grid.

    Note: As and Bs are expected to have the same length.
    
    Parameters
    ----------
    data : pd.DataFrame
        The data to plot.
    As : list of str
        The column names of the data to plot on the y-axis.
    Bs : list of str
        The column names of the data to plot on the x-axis.

    Returns
    -------
    None

    Note
    ----
    The lists As and Bs are expected to have the same length.
    """
    num_plots = len(As)
    #2 x ceil(num_plots / 2) grid ( equal to floor(num_plots+1)/ 2) )
    ncols = 2
    nrows = (num_plots + 1) // ncols

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(12, 5 * nrows))

    for i, (A, B) in enumerate(zip(As, Bs)):
        x = sorted(data[B].unique())
        y = [data[data[B] == j][A].mean() for j in x]

        row = i // ncols
        col = i % ncols

        ax = axes[row, col] if nrows > 1 else axes[col]

        ax.plot(x, y, color='black')
        ax.set_title(A + ' by ' + B)
        ax.set_xlabel(B)
        ax.set_ylabel(A)
        ax.set_aspect(1.0 / ax.get_data_ratio(), adjustable='box')

    #Hide leftover axes (if num_plots is odd)
    for j in range(num_plots, nrows * ncols):
        row = j // ncols
        col = j % ncols
        fig.delaxes(axes[row, col] if nrows > 1 else axes[col])

    plt.tight_layout()
    plt.show()

def plot_A_by_B_and_C(data, A='OREB_PCT', B='PLAYER_HEIGHT_INCHES', C='AGE'):
    """
    Plots the average value of column A by the unique values of columns B, and then by the values of C.

    Similar to running plot_A_by_B twice (with C as B column the second time), but it plots two plots
        side by side, one for A by B, and one for A by C.

    Parameters
    ----------
    data : pd.DataFrame
        The data to plot.
    A : str
        The column name of the data to plot on the y-axis.
    B : str
        The column name of the data to plot on the x-axis.
    C : str
        The column name of the data to plot on the x-axis for the second plot.

    Returns
    -------
    None
    """
    x1 = sorted(data[B].unique())
    x2 = sorted(data[C].unique())
    y1 = [data[data[B]==i][A].mean() for i in x1]
    y2 = [data[data[C]==i][A].mean() for i in x2]
    fig, ax = plt.subplots(nrows=1 ,ncols=2, figsize=(10, 6))
    sns.lineplot(x=x1, y=y1, ax=ax[0])
    sns.lineplot(x=x2, y=y2, ax=ax[1])
    ax[0].set_aspect(1.0/ax[0].get_data_ratio(), adjustable='box'); ax[1].set_aspect(1.0/ax[1].get_data_ratio(), adjustable='box')
    ax[0].set_title(A + ' by ' + B);ax[1].set_title(A + ' by ' + C)
    ax[0].set_xlabel(B);ax[1].set_xlabel(C);ax[0].set_ylabel(A);ax[1].set_ylabel(A)

def plot_As_by_Bs_and_Cs(data, As=['OREB_PCT'], Bs=['PLAYER_HEIGHT_INCHES'], Cs=['AGE']):
    """
    Plots the average value of column A by the unique values of columns B, and then by the values of C,
        for each pair of A, B, and C.
    
    The pairs of A, B, and C are the ones with the same index in the As, Bs, and Cs lists.
    Basically, it uses the plot_A_by_B_and_C function for the zip elements of As, Bs, and Cs.
    The plots are displayed in a 2-column grid, with each row corresponding to a pair of A, B, and C.

    Note: As, Bs, and Cs are expected to have the same length.

    Parameters
    ----------
    data : pd.DataFrame
        The data to plot.
    As : list of str
        The column names of the data to plot on the y-axis.
    Bs : list of str
        The column names of the data to plot on the x-axis.
    Cs : list of str
        The column names of the data to plot on the x-axis for the second plot.

    Returns
    -------
    None

    Note
    ----
    The lists As, Bs, and Cs are expected to have the same length.
    """
    num_plots = len(As)
    fig, axes = plt.subplots(nrows=num_plots, ncols=2, figsize=(12, 5 * num_plots))  # Reduced width from 20 to 12

    for i, (A, B, C) in enumerate(zip(As, Bs, Cs)):
        x1 = sorted(data[B].unique())
        x2 = sorted(data[C].unique())
        y1 = [data[data[B] == j][A].mean() for j in x1]
        y2 = [data[data[C] == j][A].mean() for j in x2]

        if num_plots == 1:
            ax1, ax2 = axes
        else:
            ax1, ax2 = axes[i]

        sns.lineplot(x=x1, y=y1, ax=ax1)
        sns.lineplot(x=x2, y=y2, ax=ax2)

        ax1.set_title(A + ' by ' + B)
        ax2.set_title(A + ' by ' + C)
        ax1.set_xlabel(B)
        ax2.set_xlabel(C)
        ax1.set_ylabel(A)
        ax2.set_ylabel(A)
        ax1.set_aspect(1.0 / ax1.get_data_ratio(), adjustable='box')
        ax2.set_aspect(1.0 / ax2.get_data_ratio(), adjustable='box')

    plt.tight_layout()
    #May add plt.subplots_adjust(wspace=0.3) too
    plt.show()

def plot_ordered(values, name):
    ordered = sorted(values)
    #print(ordered[0])
    fig, ax = plt.subplots(nrows=1 ,ncols=1, figsize=(10, 6))
    ax.plot(ordered); ax.set_title("Plot of "+name);ax.set_aspect(1.0/ax.get_data_ratio(), adjustable='box')

def plot_in_row(values, name):
    """
    Plots the linear, logarithm, and square root of the given values in a row.
    
    Parameters
    ----------
    values : list of float
        The values to plot.
    name : str
        The name of the values to use in the title of the plots.
        
    Returns
    -------
    None
    """
    ordered = sorted(values)
    log_vals_plus = [np.log(val+0.002) for val in ordered]  # I add 0.002, to not get log(0)
    sqrt_vals= np.sqrt(ordered)
    fig, ax = plt.subplots(nrows=1 ,ncols=3, figsize=(10, 6))
    ax[0].plot(ordered); ax[1].plot(log_vals_plus); ax[2].plot(sqrt_vals)
    ax[0].set_title("Linear plot of "+name); ax[1].set_title("Logarithm plot of "+name); ax[2].set_title("Sqrt plot of "+name)
    ax[0].set_aspect(1.0/ax[0].get_data_ratio(), adjustable='box'); ax[1].set_aspect(1.0/ax[1].get_data_ratio(), adjustable='box'); ax[2].set_aspect(1.0/ax[2].get_data_ratio(), adjustable='box')

def plot_in_rows(values_list, names):
    """
    Plots the linear, logarithm, and square root of the given values in rows for each list of values.

    Parameters
    ----------
    values_list : list of list of float
        The values to plot, one list for each row.
    names : list of str
        The names of the values to use in the title of the plots.

    Returns
    -------
    None
    """
    num_plots = len(values_list)
    num_cols = 3  #Columns: Linear, logarithm, sqrt
    num_rows = num_plots

    fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(15, 5 * num_rows))

    for i, (values, name) in enumerate(zip(values_list, names)):
        ordered = sorted(values)
        log_vals_plus = [np.log(val + 0.002) for val in ordered]  # Add 0.002 to avoid log(0)
        sqrt_vals = np.sqrt(ordered)

        axes[i, 0].plot(ordered)
        axes[i, 1].plot(log_vals_plus)
        axes[i, 2].plot(sqrt_vals)

        axes[i, 0].set_title("Linear plot of " + name)
        axes[i, 1].set_title("Logarithm plot of " + name)
        axes[i, 2].set_title("Sqrt plot of " + name)

        axes[i, 0].set_aspect(1.0 / axes[i, 0].get_data_ratio(), adjustable='box')
        axes[i, 1].set_aspect(1.0 / axes[i, 1].get_data_ratio(), adjustable='box')
        axes[i, 2].set_aspect(1.0 / axes[i, 2].get_data_ratio(), adjustable='box')

    plt.tight_layout()
    plt.show()

def normalized_plot_in_row(values, name):
    """
    After normalizing the given values, plots the linear, logarithm, and square root of them in a row.

    Parameters
    ----------
    values : list of float
        The values to plot.
    name : str
        The name of the values to use in the title of the plots.

    Returns
    -------
    None
    """
    ordered = sorted(values); ordered_n = (ordered-np.min(ordered))/(np.max(ordered)-np.min(ordered))
    log_vals_plus = [np.log(val+0.002) for val in ordered]; ordered_log = (log_vals_plus-np.min(log_vals_plus))/(np.max(log_vals_plus)-np.min(log_vals_plus))
    sqrt_vals= np.sqrt(ordered); ordered_sqrt = (sqrt_vals-np.min(sqrt_vals))/(np.max(sqrt_vals)-np.min(sqrt_vals))
    fig, ax = plt.subplots(nrows=1 ,ncols=3, figsize=(10, 6))
    ax[0].plot(ordered_n); ax[1].plot(ordered_log); ax[2].plot(ordered_sqrt)
    ax[0].set_title("Linear plot of "+name); ax[1].set_title("Logarithm plot of "+name); ax[2].set_title("Sqrt plot of "+name)
    ax[0].set_aspect(1.0/ax[0].get_data_ratio(), adjustable='box'); ax[1].set_aspect(1.0/ax[1].get_data_ratio(), adjustable='box'); ax[2].set_aspect(1.0/ax[2].get_data_ratio(), adjustable='box')

def plot_dendrogram(model, **kwargs):
    """The code is taken from the scikit learn documentation:
    https://scikit-learn.org/stable/auto_examples/cluster/plot_agglomerative_dendrogram.html
    """

    # Create linkage matrix and then plot the dendrogram
    # create the counts of samples under each node
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack(
        [model.children_, model.distances_, counts]
    ).astype(float)

    # Plot the corresponding dendrogram
    dendrogram(linkage_matrix, **kwargs)
